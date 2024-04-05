class PromptGenerator(object):
    def __init__(self):
        """
        Setup generation parameters for Gemma.
        """
        self.output_len = 25
        self.temperature = 0.0
        self.top_p = 1.0
        
    def create_prompt(self, sample):       
        
        prompt = """Read the following table and answer the related question based on the table.

TABLE:
Column Name: "Date","Location","Opponenent","Result","Match type"
Row 1: "29 March 2000","Debrecen","Poland","0-0 (draw)","friendly"
Row 2: "16 August 2000","Budapest","Austria","1-1 (draw)","friendly"
Row 3: "3 September 2000","Budapest","Italy","2-2 (draw)","WC -qualifier"
Row 4: "15 August 2001","Budapest","Germany","2-5 (defeat)","friendly"
Row 5: "1 September 2001","Tbilisi","Georgia","1-3 (defeat)","WC-qualifier"
Row 6: "5 September 2001","Budapest","Romania","0-2 (defeat)","WC-qualifier"
Row 7: "6 October 2001","Parma","Italy","0-0 (draw)","WC-qualifier"
Row 8: "14 November 2001","Budapest","Macedonia","5-0 (win)","friendly"
Row 9: "12 February 2002","Larnaca","Czech Rep.","0-2 (defeat)","friendly"
Row 10: "13 February 2002","Limassol","Switzerland","1-2 (defeat)","friendly"
Row 11: "8 May 2002","Pécs","Croatia","0-2 (defeat)","friendly"
Row 12: "21 August 2002","Budapest","Spain","1-1 (draw)","friendly"
Row 13: "7 September 2002","Reykjavík","Iceland","2-0 (win)","friendly"
Row 14: "12 October 2002","Stockholm","Sweden","1-1 (draw)","EC-qualifier"
Row 15: "16 October 2002","Budapest","San Marino","3-0 (win)","EC -qualifier"
Row 16: "20 November 2002","Budapest","Moldova","1-1 (draw)","friendly"
Row 17: "12 February 2003","Larnaca","Bulgaria","0-1 (defeat)","friendly"
Row 18: "29 March 2003","Chorzów","Poland","0-0 (draw)","EC -qualifier"
Row 19: "2 April 2003","Budapest","Sweden","1-2 (defeat)","EC -qualifier"
Row 20: "30 April 2003","Budapest","Luxembourg","5-1 (win)","friendly"
Row 21: "19 February 2004","Limassol","Latvia","2-1 (win)","friendly"
Row 22: "21 February 2004","Limassol","Romania","0-3 (defeat)","friendly"
Row 23: "9 February 2011","Dubai","Azerbaijan","2-0 (win)","friendly"
Row 24: "29 March 2011","Amsterdam","Netherlands","3-5 (defeat)","EC -qualifier"
Row 25: "3 June 2011","Luxembourg","Luxembourg","1-0 (win)","friendly"

QUESTION: When was the opponent Poland and the match type EC -qualifier?
Give the column name and row number from the table to answer the question.
The column name is 'Date' and the row number is 18

Read the following table and answer the related question based on the table.

TABLE:
Column Name: "Average Ranking","Competitive Finish","Couple","Number Of Dances","Total Score","Average"
Row 1: "1","1","Bridie & Craig","15","509","35.9"
Row 2: "2","3","David & Karina","12","360","30.0"
Row 3: "3","4","Patti & Sandro","10","295","29.5"
Row 4: "4","2","Anh & Luda","15","421","27.0"
Row 5: "5","9","Corinne & Csaba","3","77","25.7"
Row 6: "6","5","Mark & Linda","8","204","25.5"
Row 7: "7","8","Elka & Michael","4","100","25.0"
Row 8: "8","6","James & Olya","7","169","24.1"
Row 9: "9","7","Jessica & Serghei","5","120","24.0"

QUESTION: What is the total score when 7 is the average ranking?
Give the column name and row number from the table to answer the question.
The column name is 'Total Score' and the row number is 7"""
        
        # Example prompt        
        prompt += '\n'
        prompt += """Read the following table and answer the related question based on the table.\n\n"""
        prompt += 'TABLE:\n'
        prompt += 'Column Name: '
        prompt += ','.join(
            [f'"{cc}"' for cc in sample['table']['cols']]
        ) + '\n'
        i=1
        for row in sample['table']['rows']:
            prompt += 'Row '+ str(i)+ ': '
            i+=1
            prompt += ','.join(
                [f'"{rr}"' for rr in row]
            ) + '\n'
            if len(prompt)>7000:
                break
        prompt += '\n'
        prompt += 'QUESTION: ' + sample['question'] +'\n'
        prompt += 'Give the column name and row number from the table to answer the question.' + '\n'
        # print('prompt length is ')
        # print(len(prompt))

        return prompt
    
    def post_process(self, gen_text):
        gen_text = gen_text.split("\n")[0]
        pattern = r"The column name is \'(.+?)\' and the row number is (\d+)"

        match = re.search(pattern, gen_text)

        if match:
                column_name = match.group(1)
                row_number = int(match.group(2))
                column_name = column_name.replace("'", "")
                row_number-=1
                return_list = []
                return_pair = row_number, column_name
                return_list.append(return_pair)
                return return_list
        else:
                return_list = []
                return return_list 

    