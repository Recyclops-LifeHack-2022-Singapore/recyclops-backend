from models import Item, Category, Note, Resource

def seeds():

    # RESOURCES
    resource1 = Resource(title='Learn More about Recycling!', link='https://www.cgs.gov.sg/recycleright/how-to-recycle-right')
    resource2 = Resource(title='Electronic waste disposal locations', 
                         link='https://www.nea.gov.sg/our-services/waste-management/3r-programmes-and-resources/e-waste-management/where-to-recycle-e-waste')
    resource3 = Resource(title='Why is it important to dispose batteries properly', 
                         link='https://gsiwaste.com/battery-recycling-is-important-for-environmental-health/#:~:text=While%20throwing%20away%20batteries%20may,cadmium%2C%20lithium%2C%20and%20lead.')
    resource4 = Resource(title='Plastics and the danger to the ocean', 
                         link='https://www.biologicaldiversity.org/campaigns/ocean_plastics/#:~:text=Plastics%20pollution%20has%20a%20direct,or%20getting%20entangled%20in%20it.')
    resource5 = Resource(title='Donate to clean up the ocean!', link='https://teamseas.org/')
    resource6 = Resource(title='', link='https://www.towardszerowaste.gov.sg/recycle/where-to-recycle/')
    resource7 = Resource(title='',
                         link='https://www.nea.gov.sg/our-services/waste-management/3r-programmes-and-resources/e-waste-management/where-to-recycle-e-waste')

    resources =  [resource1, resource2, resource3, resource4, resource5, resource6, resource7]
    
    # NOTES

    note1 = Note(text='Glossy and Non-Glossy included')
    note2 = Note(text='With and without plastic window')
    note3 = Note(text='Donate if it is in good condition')
    note4 = Note(text='Please flattern before recycling')
    note5 = Note(text='Please empty and rinse when necessary')
    note6 = Note(text='Dispose as general waste')
    note7 = Note(text='Mineral water bottle, Soft drink bottle, Carbonated drink bottle, Milk bottle, Water bottle, Medicine bottle, etc.')
    note8 = Note(text='Shampoo, Bodywash, Facial cleanser, detergent, soap, etc.')
    note9 = Note(text='Magazine wrapper, Plastic packaging for packet drink, Bubble Wrap, Fruit Box, Ziplock Bag')
    note10 = Note(text='Please empty contents')
    note11 = Note(text='Potato chip bags, Empty blister packs, expired credit cards, etc.')
    note12 = Note(text='Packagings that are contaminated with food/oil stains')
    note13 = Note(text='Beer bottle, Wine bottle, Liquor Bottle, etc.')
    note14 = Note(text='Sauce and Condiment bottle, Jam spread bottle, Food jar, etc.')
    note15 = Note(text='Drinking glass, Wine glass, etc.')
    note16 = Note(text='Can be recycled at specific collection points')
    note17 = Note(text='Carbonated drink can, Soft drink can, Beer can')
    note18 = Note(text='Rusted metals should be disposed as general waste')
    note19 = Note(text='Biscuit and Food tin, Metal containers')
    note20 = Note(text='Make sure that they are completely metal')
    note21 = Note(text='Can be recycled at e-waste collection points here')
    note22 = Note(text='Bulky item removal service by TCs for HDB residents')
    note23 = Note(text='E-waste collection drive (Quarterly)')
    note24 = Note(text='Doorstep collection (fees may apply)')
    note25 = Note(text='To find out where you can recycle your e-waste, visit here.')
    note26 = Note(text='E-waste bins (non-ALBA)* (items must fit the opening of bins)')
    note27 = Note(text='Cash-for-Trash stations organised by Public Waste Collectors (please contact your PWCs to check that they are able to accept the e-waste)')
    note28 = Note(text='Contact Town council to remove from your residential premises')

    note21.resource = resource7
    note25.resource = resource7

    notes = [note1, note2, note3, note4, note5, note6, note7, note8, note9, note10,
             note11, note12, note13, note14, note15, note16, note17, note18, note18, note20,
             note21, note22, note23, note24, note25, note26, note27, note28]

    # CATEGORIES

    category1 = Category(name='Paper', color='#FEA656')
    category2 = Category(name='Plastic', color='#3ac9fc')
    category3 = Category(name='Glass', color='#9c9a9a')
    category4 = Category(name='Metal', color='#b780ff')
    category5 = Category(name='Others', color='#92fa87')

    categories = [category1, category2, category3, category4, category5]

    # ITEMS
    
    item1 = Item(name='Printed paper', isRecyclable=True)
    item2 = Item(name='Writing paper', isRecyclable=True)
    item3 = Item(name='Newspaper', isRecyclable=True)
    item4 = Item(name='Flyer', isRecyclable=True)
    item5 = Item(name='Brochure', isRecyclable=True)
    item6 = Item(name='Magazine', isRecyclable=True)
    item7 = Item(name='Books / Textbooks', isRecyclable=True)
    item8 = Item(name='Envelope', isRecyclable=True)
    item9 = Item(name='Red Packet', isRecyclable=True)
    item10 = Item(name='Gift Wrapping Paper', isRecyclable=True)
    item11 = Item(name='Shredded Paper', isRecyclable=True)
    item12 = Item(name='Paper Receipt', isRecyclable=True)
    item13 = Item(name='Cardboard Box / Carton Box', isRecyclable=True)
    item14 = Item(name='Paper Box / Packaging', isRecyclable=True)
    item15 = Item(name='Egg Tray', isRecyclable=True)
    item16 = Item(name='Beverage Carton (Milk, Juice, Drink)', isRecyclable=True)
    item17 = Item(name='Toilet Roll Tube', isRecyclable=True)
    item18 = Item(name='Tissue Box', isRecyclable=True)
    item19 = Item(name='Paper bag', isRecyclable=True)
    item20 = Item(name='Paper Disposable (Cups/Plates)', isRecyclable=False)
    item21 = Item(name='Paper Towel, Tissue Paper', isRecyclable=False)
    item22 = Item(name='Toilet Paper', isRecyclable=False)
    item23 = Item(name='Wooden Chopsticks', isRecyclable=False)
    item24 = Item(name='Pizza Boxes', isRecyclable=False)
    item25 = Item(name='Wax Paper', isRecyclable=False)
    item26 = Item(name='Paper packaging with food', isRecyclable=False)
    item27 = Item(name='Plastic Bottle/Container (Food/Beverage)', isRecyclable=True)
    item28 = Item(name='Plastic Bottle/Container (Non-food)', isRecyclable=True)
    item29 = Item(name='CD/DVD Casing', isRecyclable=True)
    item30 = Item(name='Plastic Bag / Packaging', isRecyclable=True)
    item31 = Item(name='Plastic Film', isRecyclable=True)
    item32 = Item(name='Plastic Clothes Hanger', isRecyclable=True)
    item33 = Item(name='Plastic Takeaway Food Container/Cup', isRecyclable=True)
    item34 = Item(name='Polystyrene foam product (Styrofoam Cup)', isRecyclable=False)
    item35 = Item(name='Plastic Disposables (Cutlery/Straw) ', isRecyclable=False)
    item36 = Item(name='Plastic Packaging with foil', isRecyclable=False)
    item37 = Item(name='Oxo- and Bio-Degradable bags', isRecyclable=False)
    item38 = Item(name='Plastic Packaging with food', isRecyclable=False)
    item39 = Item(name='Beverage Glass Bottle', isRecyclable=True)
    item40 = Item(name='Food Glass Bottle', isRecyclable=True)
    item41 = Item(name='Cosmetic/Perfume Glass Bottle', isRecyclable=True)
    item42 = Item(name='Medicine and Supplement Glass Bottle', isRecyclable=True)
    item43 = Item(name='Glassware (Cup/Plate/Glass)', isRecyclable=True)
    item44 = Item(name='Tempered Glass, Crystal Glass', isRecyclable=False)
    item45 = Item(name='Windows', isRecyclable=False)
    item46 = Item(name='Mirrors', isRecyclable=False)
    item47 = Item(name='Ceramic Products (Plate/Porcelain)', isRecyclable=False)
    item48 = Item(name='Light Bulbs (Lamp/LED)', isRecyclable=False)
    item49 = Item(name='Beverage Metal Can', isRecyclable=True)
    item50 = Item(name='Food Metal Can', isRecyclable=True)
    item51 = Item(name='Metal Bottle Cap', isRecyclable=True)
    item52 = Item(name='Clean Aluminium Tray and Foil', isRecyclable=True)
    item53 = Item(name='Non-food Metal Container (Paint Cans)', isRecyclable=True)
    item54 = Item(name='Rusty Metal Cans, Dirty Aluminium Foil/Tray', isRecyclable=False)
    item55 = Item(name='Metal Cutlery, Steel wool, Metal accessories', isRecyclable=False)
    item56 = Item(name='Desktop Computer, Laptop, Tablet, Mobile Phones, Monitors', isRecyclable=True)
    item57 = Item(name='Computer Battery, Mobile Phone battery, Battery Charger, Portable Charger', isRecyclable=True)
    item58 = Item(name='Printer, Modem, Router, Hard Disk, Keyboard, Mouse', isRecyclable=True)
    item59 = Item(name='Electronic Waste (Used mobile phone, laptop)', isRecyclable=True)
    item60 = Item(name='Household Battery, Alkaline Battery, Rechargable Battery', isRecyclable=True)
    item61 = Item(name='Refrigerators, Washing Machine, Television, Air Conditioner, PMDs', isRecyclable=True)
    item62 = Item(name='Rice Cooker, Microwave Oven, Electric Fan, Vacuum Cleaner, Gaming Console', isRecyclable=True)
    item63 = Item(name='Clothes/Shoes/Bags in good condition', isRecyclable=True)
    item64 = Item(name='Clothes/Shoes/Bags not in good condition', isRecyclable=False)
    item65 = Item(name='Food waste, Leftover medicine', isRecyclable=False)
    item66 = Item(name='Bulky waste (Furniture, Standing fan)', isRecyclable=False)

    item1.category = category1
    item2.category = category1
    item3.category = category1
    item4.category = category1
    item5.category = category1
    item6.category = category1
    item7.category = category1
    item8.category = category1
    item9.category = category1
    item10.category = category1
    item11.category = category1
    item12.category = category1
    item13.category = category1
    item14.category = category1
    item15.category = category1
    item16.category = category1
    item17.category = category1
    item18.category = category1
    item19.category = category1
    item20.category = category1
    item21.category = category1
    item22.category = category1
    item23.category = category1
    item24.category = category1
    item25.category = category1
    item26.category = category1
    item27.category = category2
    item28.category = category2
    item29.category = category2
    item30.category = category2
    item31.category = category2
    item32.category = category2
    item33.category = category2
    item34.category = category2
    item35.category = category2
    item36.category = category2
    item37.category = category2
    item38.category = category2
    item39.category = category3
    item40.category = category3
    item41.category = category3
    item42.category = category3
    item43.category = category3
    item44.category = category3
    item45.category = category3
    item46.category = category3
    item47.category = category3
    item48.category = category3
    item49.category = category4
    item50.category = category4
    item51.category = category4
    item52.category = category4
    item53.category = category4
    item54.category = category4
    item55.category = category4
    item56.category = category5
    item57.category = category5
    item58.category = category5
    item59.category = category5
    item60.category = category5
    item61.category = category5
    item62.category = category5
    item63.category = category5
    item64.category = category5
    item65.category = category5
    item66.category = category5

    items = [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, 
             item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, 
             item21, item22, item23, item24, item25, item26, item27, item28, item29, item30, 
             item31, item32, item33, item34, item35, item36, item37, item38, item39, item40, 
             item41, item42, item43, item44, item45, item46, item47, item48, item49, item50, 
             item51, item52, item53, item54, item55, item56, item57, item58, item59, item60, 
             item61, item62, item63, item64, item65, item66]

    return resources + notes + categories + items
