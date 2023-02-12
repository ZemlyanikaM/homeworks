from ui import ch_mode    
import ui
import rational as r
import complex as c

 
if ch_mode() == 1:
    ui.outp(r.calcr(ui.input_r()))
else:
    ui.outp(c.calcc(ui.input_c()))

