# Load cmoi base ssm domaine
rpy.show_levels -i \
   $CMCGRIDF/prog/glbhyb/$(date +%Y%m%d00)_000\
   $CMCGRIDF/prog/reghyb/$(date +%Y%m%d00)_000\
   $CMCGRIDF/prog/lam/nat.model/$(date +%Y%m%d00)_000\
   --vcode\
   --ptop_graph 100700\
   --pbot_hill 101325\
   --ptop_hill 101325\
   --title ETIKET\
   --plot_thermo\
   --legend_text_spacing .12\
   --out fig5.png
