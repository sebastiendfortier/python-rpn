VGRID_SAMPLE=${ATM_MODEL_DFILES}/bcmk_vgrid

rpy.show_levels -i \
   ${VGRID_SAMPLE}/5005\
   ${VGRID_SAMPLE}/5100\
   --vcode\
   --title ETIKET\
   --hide_diag\
   --plot_width 10\
   --small_scale_topo_cycles 30.\
   --small_scale_topo_amp 50000.\
   --out fig10.png


