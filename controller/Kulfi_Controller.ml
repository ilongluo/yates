open Kulfi_Routing
open Kulfi_MCF

module Make(SOLVER:Kulfi_Routing.Algorithm) = struct    
  let start () = ()
end

module Controller = Make(Kulfi_Routing.Mcf)

let () =
  print_endline "Kulfi Controller";
  Controller.start()