import pywhatkit as pw

txt = """Why was DJI Fly removed from playstore?
Because the compatibility strategy between the DJI App and Google Play Store is changing, you currently cannot finish downloading and updating using Google Play.
To ensure your usage, we have launched a DJI official download channel."""

pw.text_to_handwriting(txt, "demo1.jpg", [0,0,138])
print(" END ")