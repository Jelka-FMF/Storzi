
type color = RGB of (int * int * int)
type position = { id: int; x: float; y: float; z: float }
type mode = SIX | SEVEN

let line_to_pos line =
  match line with
  | id :: x :: y :: z :: [] -> {id = int_of_string id; x = float_of_string x; y = float_of_string y; z = float_of_string z}
  | _ -> failwith "Unexpected position format"

let positions: 'position list =
  In_channel.with_open_text (
    match Sys.getenv_opt "JELKA_POSITIONS" with
    | Some s -> s
    | None -> "../../data/positions.csv"
    ) (fun ic ->
    In_channel.input_lines ic |> List.map (String.split_on_char ',') |> List.map line_to_pos)

let led_count = List.length positions

let print_hex (i: int) = (
    if i < 0 || i > 255 then failwith "Invalid color value";
    let hx = ['0'; '1'; '2'; '3'; '4'; '5'; '6'; '7'; '8'; '9'; 'A'; 'B'; 'C'; 'D'; 'E'; 'F'] in
    i / 16 |> List.nth hx |> print_char;
    i mod 16 |> List.nth hx |> print_char
)

let print_frame (frame: color list) = (
    if List.length frame <> led_count then failwith "Invalid frame length";
    print_char '#';
    List.iter (function RGB (r, g, b) -> print_hex r; print_hex g; print_hex b) frame;
    print_endline ""
)

let sq x = x *. x

let dist2 x1 y1 x2 y2 =
  sq (x1 -. x2) +. sq (y1 -. y2)

let at_line x1 y1 x2 y2 d x y =
  let k = (x1 -. x2) /. (y1 -. y2) in
  let  n = x1 -. k *. y1 in
  let to_x y = k *. y +. n in
  (y1 -. y) *. (y2 -. y) < 0.
  && (x1 -. x) *. (x2 -. x) < 0.
  && sq (x -. to_x y) < sq d

let is_six x y =
  let in_outer_circ = (dist2 x y 0. 30.) < 350. in
  let outside_inner_circ = (dist2 x y 0. 30.) > 100. in
  let at_top = at_line (-10.) 45. 20. 70. 5. x y in
  (in_outer_circ && outside_inner_circ) || at_top

let is_seven x y =
  at_line 0. 10. 15. 50. 5. x y
  || (abs_float (y -. 55.) < 5. && abs_float x < 20.)


let makedigit (positions: position list) (m: mode) (color: color) (bgcolor: color) : color list =
  let set_colors fn = List.map (
    fun pos -> match fn pos.x pos.z with
    | true -> color
    | false -> bgcolor ) positions
  in
  match m with
  | SIX -> set_colors is_six
  | SEVEN ->  set_colors is_seven


let evolution = [92; 208; 263; 429; 557; 675; 795; 894; 1017; 1169; 1284; 1350; 1539; 1728; 1788; 1937; 2077; 2133; 2178; 2314; 2497; 2603; 2765; 2933; 2984; 3120; 3184; 3225; 3387; 3449; 3582; 3739; 3831; 3975; 4035; 4116; 4290; 4341; 4434; 4558; 4738; 4868; 4958; 5105; 5253; 5346; 5507; 5549; 5686; 5872; 5987; 6156; 6252; 6385; 6428; 6592; 6713; 6807; 6917; 6951; 7123; 7268; 7403; 7546; 7696; 7753; 7902; 7935; 8109; 8196; 8368; 8508; 8640; 8831; 8975; 9029]
let change m = match m with | SIX -> SEVEN | SEVEN -> SIX

let rec loop duration m = (
    let m = match List.find_opt (( = ) duration)  evolution with
      | Some _ -> change m
      | None -> m in
    let frame = makedigit positions m (RGB(255, 0, 0)) (RGB(0, 150, 0)) in
    print_frame frame;
    if duration > 0 then (
        loop (duration - 1) m
    ) else ()
)

;;

let fps = 50 in

Printf.printf "#{\"version\": 0, \"led_count\": %d, \"fps\": %d}\n" led_count fps;

loop (180 * fps) SIX;;