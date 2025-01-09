#load "unix.cma";;

let stevilo_luck : int = 500
let skok_stopnje = 9 (*Mora biti liho število*)
let skok_pozicije = 1 (*Mora biti deljivo z skok_stopnje*)

let barve = [|
"f4ebfe"; "efe3fd"; "ebdbfd"; "e7d3fd"; "e3ccfc"; "dec4fc";
"dabcfc"; "d6b4fc"; "d1acfb"; "cda4fb"; "c99cfb"; "c595fa";
"c08dfa"; "bc85fa"; "b87df9"; "b375f9"; "af6df9"; "ab65f8";
"a75ef8"; "a256f8"; "9e4ef7"; "9a46f7"; "953ef7"; "9136f6";
"8d2ff6"; "8927f6"; "841ff6"; "8017f5"; "7c0ff5"; "7709f3";
"7409eb"; "7009e3"; "6c08db"; "6808d3"; "6408cc"; "6007c4";
"5c07bc"; "5907b4"; "5506ac"; "5106a4"; "4d069c"; "490595";
"45058d"; "410585"; "3d057d"; "3a0475"; "36046d"; "320466";
"2e035e"; "2a0356"; "26034e"; "220246"; "1e023e"; "1b0236"
|]
let n = Array.length barve 
let stopnje = Array.init n (fun i -> (i + 1) * skok_stopnje)
let polozaji = Array.make n 1

let rec po_framih frame = 
  let lucke = Array.make stevilo_luck "000000" in

  let spremeni_polozaje = 
    let rec po_polozajih s = 
      if s < n && stopnje.(s) <> 0 then
        match stopnje.(s) with
        | x when x mod 2 = 0 -> 
          polozaji.(s) <- (polozaji.(s) + skok_pozicije) ; 
          po_polozajih (s + 1)
        | _ -> 
          polozaji.(s) <- (polozaji.(s) - skok_pozicije) ; 
          po_polozajih (s + 1)
    in
    po_polozajih 0
  in

  let spremeni_stopnje = 
    let rec po_barvah s =
      if s < n then
        match polozaji.(s) mod stopnje.(s) with
        | 0 -> 
          stopnje.(s) <- (stopnje.(s) + skok_stopnje - 1) mod stevilo_luck + 1 ; 
          po_barvah (s + 1)
        | _ -> po_barvah (s + 1)
      in
    po_barvah 0
  in

  let rec po_luckah i = 
    if i < stevilo_luck then
      let rec po_barvah s =
        if s < n then
          match i with
          | _ when polozaji.(s) = i -> 
            lucke.(i) <- barve.(s) ;
            po_barvah (s + 1)
          | _ -> po_barvah (s + 1)
      in
    po_barvah 0;
    po_luckah (i + 1)
  in


  po_luckah 0;
  print_char '#';
  (* let lucke_reversed = Array.of_list (List.rev (Array.to_list lucke)) in *)
  Array.iter print_string lucke;
  print_char '\n';
  spremeni_polozaje;
  spremeni_stopnje;

  Unix.sleepf (1. /. 50.);

  match frame with
  | _ -> po_framih (frame + 1);

;;

print_string "#{\"version\":0, \"led_count\":500, \"fps\":5}\n";;
po_framih 0;;
