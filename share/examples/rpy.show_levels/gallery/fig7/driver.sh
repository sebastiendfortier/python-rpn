VGRID_SAMPLE=${ATM_MODEL_DFILES}/bcmk_vgrid

rpy.show_levels -i \
   ${VGRID_SAMPLE}/sigma\
   ${VGRID_SAMPLE}/eta\
   ${VGRID_SAMPLE}/5001\
   ${VGRID_SAMPLE}/5005\
   ${VGRID_SAMPLE}/5100\
   --vcode\
   --allow_sigma\
   --title ETIKET\
   --plot_width 2.5\
   --hide_diag_levels\
   --out fig1.png

