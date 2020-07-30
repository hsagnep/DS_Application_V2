from flask import Flask, render_template,Markup
'''
    #Content Template
    {
        'Header' : '',
        'Paragraph' : [],
        'List_Items' : [{'Title' : 'List Title',
                        'li' : ['List Item','List Item']},],
        'Formula' : [{'Formulae' : Markup('<h3 class="text-center">Q<sub>BEP</sub>=FC/(p-v)</h3>'),
                    'Formulae_Vars' : []}],
        'Images' : ['index_image.jpg']
    },
    #Terms Template
    {
    'Term' : '',
    'Definition' : ''
    },  

'''

content = [
    {
        'Header' : 'Why Carry Inventory?',
        'Paragraph' : [],
        'List_Items' : [{'Title' : '',
                        'li' : ['Need to meet anticipated demand','To protect against stock-outs','To smooth production requirements, de-couple components of the production-distribution, and/or permit operations (pipeline inventory)','To help hedge against price increases or to take advantage of quantity discounts or order cycles']},],
        'Formula' : [{'Formulae' : Markup('<h3 class="text-center">Q<sub>BEP</sub>=FC/(p-v)</h3>'),
                    'Formulae_Vars' : ['Q = Quantity', 'FC = Fixed Cost', 'p = Price','v = Variable']}]
    },
{
        'Header' : 'Header',
        'Paragraph' : ['Paragraph'],
        'List_Items' : [{'Title' : 'List Title',
                        'li' : ['List Item','List Item']},],
        'Formula' : [{'Formulae' : Markup('<h3 class="text-center">Q<sub>BEP</sub>=FC/(p-v)</h3>'),
                    'Formulae_Vars' : ['Q = Quantity', 'FC = Fixed Cost', 'p = Price','v = Variable']}]
    },
]

key_terms = [{
    'Term' : 'Forecasting',
    'Definition' : 'Techniques consist of a sequence of steps that will lead to an optimal solution to problems, in cases where a solution exists, given restrictions or limitations.'
},
{'Term' : 'Mean Average Deviation',
'Definition' : 'Test!'
},
{'Term' : 'Mean Average Deviation',
'Definition' : 'Test!'
},
]

IM_Content = [
    {
        'Header' : 'Why Carry Inventory?',
        'Paragraph' : [],
        'List_Items' : [{'Title' : '',
                        'li' : ['Need to meet anticipated demand','To protect against stock-outs','To smooth production requirements, de-couple components of the production-distribution, and/or permit operations (pipeline inventory)','To help hedge against price increases or to take advantage of quantity discounts or order cycles']},],
    },
{
        'Header' : 'Requirements for Effective Inventory Management',
        'Paragraph' : [],
        'List_Items' : [{'Title' : '',
                        'li' : ['A system to keep track of inventory','A reliable forecast of demand','Knowledge of lead times','Reasonable estimates of holding, ordering, and shortage costs']},],
    },

    {
        'Header' : 'Inventory Counting Systems',
        'Paragraph' : [],
        'List_Items' : [{'Title' : '',
                        'li' : ['Periodic System - Physical count of items made at periodic intervals ','Perpetual Inventory System - System that keeps track of removals from inventory continuously, thus monitoring current levels of each item']},],
    },
    {
        'Header' : 'What is the Economic Quantity to Order?',
        'Paragraph' : [],
        'List_Items' : [{'Title' : 'EOQ Assumptions:',
                        'li' : ['Only one product is involved','Demand is even throughout the year','Lead time does not vary','Each order is received in a single delivery','There are no quantity discounts']}],
    },
        {
        'Header' : 'Ordering Costs',
        'Paragraph' : [],
        'List_Items' : [{'Title' : '',
                        'li' : ['If the annual demand D for an item, and each item costs p, we will spend p*D over the course of the year to meet this demand, regardless of order size.','If the order size is Q, the frequency of orders during the year is D/Q','Each order placed incurs a fixed cost, S, which is assumed to be independent of the size of the order','The annual variable order costs are p*D and the fixed order costs are (D/Q)*S, with larger Q resulting in lower ordering costs',]}],
    },
]

IM_Key_Terms =[
    {
        'Term' : 'Holding Costs (H)',
        'Definition' : 'Also known as carrying cost; The cost to carry an item in inventory for a length of time, usually a year.'
    },
    {
        'Term' : 'Ordering Costs (s)',
        'Definition' : 'Costs of ordering and receiving inventory.'},
{
        'Term' : 'Shortage Costs',
        'Definition' : 'Costs when demand exceeds supply.'
},
{
        'Term' : 'Lead Time',
        'Definition' : 'The time interval between ordering and receiving an order.'
},
]

FC_Content = [
    {
        'Header' : 'Forecast Time Horizons',
        'Paragraph' : [],
        'List_Items' : [{'Title' : '',
                        'li' : ['Short-range (Immediate future to 3 months)','Medium-range (Several months to a year)','Long range (More than one year)']},],
    },
{
        'Header' : 'Common Aspects of Forecasts',
        'Paragraph' : [],
        'List_Items' : [{'Title' : '',
                        'li' : ['A system to keep track of inventory','A reliable forecast of demand','Knowledge of lead times','Reasonable estimates of holding, ordering, and shortage costs']},],
    },

    {
        'Header' : 'Types of Forecasts',
        'Paragraph' : [],
        'List_Items' : [{'Title' : '',
                        'li' : ['Periodic System - Physical count of items made at periodic intervals ','Perpetual Inventory System - System that keeps track of removals from inventory continuously, thus monitoring current levels of each item']},],
    },
    {
        'Header' : 'What is the Economic Quantity to Order?',
        'Paragraph' : [],
        'List_Items' : [{'Title' : 'EOQ Assumptions:',
                        'li' : ['Only one product is involved','Demand is even throughout the year','Lead time does not vary','Each order is received in a single delivery','There are no quantity discounts']}],
    },
        {
        'Header' : 'Ordering Costs',
        'Paragraph' : [],
        'List_Items' : [{'Title' : '',
                        'li' : ['If the annual demand D for an item, and each item costs p, we will spend p*D over the course of the year to meet this demand, regardless of order size.','If the order size is Q, the frequency of orders during the year is D/Q','Each order placed incurs a fixed cost, S, which is assumed to be independent of the size of the order','The annual variable order costs are p*D and the fixed order costs are (D/Q)*S, with larger Q resulting in lower ordering costs',]}],
    },
]

FC_Key_Terms =[
    {
        'Term' : 'Time series ',
        'Definition' : 'Uses historical data assuming the future will be like the past.'
    },
]

