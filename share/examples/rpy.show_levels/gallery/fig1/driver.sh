VGRID_SAMPLE=${ATM_MODEL_DFILES}/bcmk_vgrid

rpy.show_levels -i \
   ${VGRID_SAMPLE}/sigma\
   ${VGRID_SAMPLE}/eta\
   ${VGRID_SAMPLE}/5001\
   ${VGRID_SAMPLE}/5005\
   ${VGRID_SAMPLE}/5100\
   ${VGRID_SAMPLE}/21001_NON_SLEVE\
   ${VGRID_SAMPLE}/21001_SLEVE\
   ${VGRID_SAMPLE}/21002_NON_SLEVE\
   ${VGRID_SAMPLE}/21002_SLEVE\
   --vcode\
   --allow_sigma\
   --title ETIKET\
   --scale_fonts .8\
   --plot_width 2.2\
   --out fig1.png

