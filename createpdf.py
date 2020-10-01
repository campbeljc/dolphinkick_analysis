from fpdf import FPDF
import os

temp_destination = '/Users/jennacampbell/Desktop'

def create_pdf(name, orientation, gender, speed, fig1_dest, fig2_dest, fig3_dest, destination=temp_destination):

    pdf = FPDF()
    pdf.add_page()  
    pdf.set_font('Arial', 'B', 16)
    pdf.ln()
    pdf.ln()

    title = "Dolphin Kick Analysis for {name}".format(name=name)
    pdf.cell(0, 8, title, 0, 1,'C')

    pdf.set_font('Arial', '', 11)
    gender_text = "Gender: {gender}".format(gender=gender)
    orientation_text = "Orientation: {orientation}".format(orientation=orientation)
    speed_text = "Speed: {speed}".format(speed=speed)
    pdf.cell(65,10,gender_text,0,0,'C')
    pdf.cell(65,10,orientation_text,0,0,'C')
    pdf.cell(65,10,speed_text,0,1,'C')

    pdf.set_font('Arial','B',12)
    graph1_title = 'Vertical Variation Over Time'
    graph3_title = 'Time Decomposition'
    pdf.cell(82,8,graph1_title,0,0,'C')
    pdf.cell(120,8,graph3_title,0,1,'C')

    pdf.image(fig1_dest, x=8, y=35, w=80)
    pdf.image(fig3_dest, x=95, y=35, w=110)

    graph2_title = 'Comparison with Elite Swimmers'
    graph2_subtitle = 'Figure shows comparison of vertical displacement of key joints on swimmers body with average vertical displacement of key joints from professional swimmers during four distinct time points within the kick. All statistically significant differences are marked red.'
    pdf.set_xy(x=10,y=110)
    pdf.set_font('Arial','B',14)
    pdf.cell(0,8, graph2_title,0,1,'C')
    pdf.set_font('Arial','',9)

    pdf.image(fig2_dest,x=15, y=120, w=190)
    pdf.set_xy(x=10,y=240)
    pdf.ln()
    pdf.multi_cell(0,5, graph2_subtitle,0,1,'C')

    file_name = name + "_dolphinkickanalyis"'.pdf'
    save_path = os.path.join(destination, file_name)

    pdf.output(save_path, 'F')

    return pdf