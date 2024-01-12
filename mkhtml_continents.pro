; Makes fire dashboard landing page for countries

; Which version to make?
iver=0    ; 0=yearly
fnhtml='table-for-fire-countries-yearly.html'

; Read list of countries with continent indicators

fnlist='continents_table.csv'
print,'Reading continents and countries from:'
print,fnlist
rawdat=read_csv(fnlist,header=cnthead)

; This creates rawdat as a structure of arrays, i.e. rawdat.field01
; is an N-element vector containing the first column from the csv file.

; Extract continent names (skip first 3 field names)
cntnm=cnthead[3:*]
ncnt=n_elements(cntnm)

; Create html for a list of countries, grouped by continent, where
; each entry is a link to the yearly page for that country.
; This is not a complete html file, it is meant to be pasted into an existing
; html file that contains the rest of the webpage and the styles etc.

print,'Writing to: '+fnhtml
openw,l1,/get_lun,fnhtml

; Process each continent in turn

cntcount=fltarr(ncnt)    ; count how many countries are associated with each continent

for icnt = 0 , ncnt-1 do begin

 ; Find which countries I've assigned to this continent

 flaglist=rawdat.(icnt+3)     ; extracts fieldNN where NN=icnt+3
 gotlist=where(flaglist gt 0,ngot)
 print
 print,cntnm[icnt],ngot

 ; Extract fields for this subset of countries

 if ngot gt 0 then begin

  cysubsetno=(rawdat.field01)[gotlist]   ; country number
  cysubsetab=(rawdat.field02)[gotlist]   ; country abbreviation
  cysubsetnm=(rawdat.field03)[gotlist]   ; country name

  ; Sort into alphabetical order by abbreviation

  isort=sort(cysubsetab)
  print,cysubsetab[isort]

  ; Generate HTML entry for this continent, followed by 1-line per country

  printf,l1,'<h4>'+cntnm[icnt]+'</h4>'
  printf,l1
  printf,l1,'<ol>'
  for i = 0 , ngot-1 do begin
   j=isort[i]
   urlname=cysubsetab[j]+'/yearly.html'
   printf,l1,'  <li><href="'+urlname+'">'+cysubsetab[j]+' &nbsp;&nbsp;&nbsp; '+cysubsetnm[j]+'</href></li>'
  endfor
  printf,l1,'</ol>'
  printf,l1

 endif

endfor

free_lun,l1

end
