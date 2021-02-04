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
   --plot_thermo\
   --plot_vertical_velocity\
   --legend_fraction .35\
   --legend_text_spacing .09\
   --scale_fonts .8\
   --plot_width 2.5\
   --out fig2.png
