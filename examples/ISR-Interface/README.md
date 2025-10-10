This example contains a methanol liquid-vapor interface. A reference state is assigned to each methanol according to the global z distance (see the associated work for details: https://doi.org/10.1063/5.0244427). The ISR method is then employed to recast this state assignment in terms of the local neighbor environment of the CG methanol sites. To complete this example:

1. Download all files.
2. Run 
 ```
cgisr @cgisr.args
 ```
This produces a file 'isr.dat' which contains the parameters for UCGRLECUSTOM for further UCG force-field parameterization via the UCG FM or UCG REM methods. Note that the 'VAL' terms in 'isr.dat' must be changed to reflect the actual CG bead type after running cgisr.