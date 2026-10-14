(* Advent of Code 2022, jour 1.
   Lecture récursive des blocs (séparés par une ligne vide), somme de chaque
   bloc avec List.fold_left, puis maximum (partie 1) et somme des trois plus
   grands après un tri décroissant (partie 2). *)

let elves =
  let f = open_in "input" in
  let rec read_elf () =
    try
      match input_line f with
      | "" -> [] (* fin d'un bloc *)
      | l -> int_of_string l :: read_elf ()
    with End_of_file -> [] (* dernière ligne *)
  in
  let rec read_elves () =
    match read_elf () with
    | [] -> []
    | e -> e :: read_elves ()
  in
  read_elves ()

let elves_cal = List.map (List.fold_left ( + ) 0) elves

let () =
  Printf.printf "Partie 1 : %d\n" (List.fold_left max 0 elves_cal);
  let v =
    match List.sort (fun a b -> b - a) elves_cal with
    | e1 :: e2 :: e3 :: _ -> e1 + e2 + e3
    | _ -> failwith "moins de trois blocs"
  in
  Printf.printf "Partie 2 : %d\n" v
