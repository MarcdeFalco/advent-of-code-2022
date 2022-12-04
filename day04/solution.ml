let f = open_in "input.txt"

let elves : ((int * int) * (int * int)) list = 
    let get_elf s =
        match String.split_on_char '-' s with
        | [a;b] -> int_of_string a, int_of_string b
        | _ -> failwith "unreachable" in
    let rec read_elves () =
        try
            let l = input_line f in
            let (a,b), (c,d) =
                match String.split_on_char ',' l with
                | [e1;e2] -> (get_elf e1, get_elf e2)
                | _ -> failwith "unreachable" in
            ( (a,b), (c,d) ) :: read_elves ()
        with End_of_file -> [] in
    read_elves ()

let countains ((a,b), (c,d)) =
    (a <= c && d <= b) || (c <= a && b <= d)

let overlaps ((a,b), (c,d)) =
    (a <= c && c <= b) || (c <= a && a <= d)

let _ =
    Printf.printf "Part 1: %d\n"
        (List.length (List.filter countains elves));
    Printf.printf "Part 2: %d\n"
        (List.length (List.filter overlaps elves))
