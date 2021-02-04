VGRID_SAMPLE=${ATM_MODEL_DFILES}/bcmk_vgrid

rpy.show_levels -i \
   ${VGRID_SAMPLE}/21002_SLEVE\
   --vcode\
   --allow_sigma\
   --title ETIKET\
   --plot_thermo\
   --plot_vertical_velocity\
   --legend_fraction .5\
   --legend_text_spacing .09\
   --plot_width 8\
   --scale_fonts 1.5\
   --out fig8.png
