(* Advent of Code 2022, jour 4.
   Lecture des paires d'intervalles avec String.split_on_char, puis comptage
   avec List.filter des paires dont un intervalle contient l'autre (partie 1)
   et de celles qui se chevauchent (partie 2). *)

let f = open_in "input.txt"

let elves : ((int * int) * (int * int)) list =
  let get_elf s =
    match String.split_on_char '-' s with
    | [ a; b ] -> (int_of_string a, int_of_string b)
    | _ -> failwith "intervalle mal formé"
  in
  let rec read_elves () =
    try
      let l = input_line f in
      let pair =
        match String.split_on_char ',' l with
        | [ e1; e2 ] -> (get_elf e1, get_elf e2)
        | _ -> failwith "ligne mal formée"
      in
      pair :: read_elves ()
    with End_of_file -> []
  in
  read_elves ()

let contains ((a, b), (c, d)) = (a <= c && d <= b) || (c <= a && b <= d)

let overlaps ((a, b), (c, d)) = (a <= c && c <= b) || (c <= a && a <= d)

let () =
  Printf.printf "Partie 1 : %d\n" (List.length (List.filter contains elves));
  Printf.printf "Partie 2 : %d\n" (List.length (List.filter overlaps elves))
