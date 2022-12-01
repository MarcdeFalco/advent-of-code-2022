let elves =
    let f = open_in "input" in
    let rec read_elf () =
        try
            match input_line f with
            | "" -> [] (* end of batch *)
            | l -> int_of_string l :: read_elf ()
        with End_of_file -> [] (* for last line *)
    in
    let rec read_elves () =
        match read_elf () with
        | [] -> []
        | e -> e :: read_elves ()
    in read_elves ()

let elves_cal = 
    List.map (List.fold_left (+) 0) elves

let part1 = 
    Printf.printf "Part 1 : %d\n"
        (List.fold_left max 0 elves_cal)

let part2 =
    let v = match List.sort (fun a b -> b-a) elves_cal with
    | e1::e2::e3::_ -> e1+e2+e3
    | _ -> failwith "Unreachable"
    in Printf.printf "Part 2 : %d\n" v
