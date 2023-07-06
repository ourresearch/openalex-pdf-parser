# Parseland

This API parses and returns author, affiliation, full text, and reference/citation data from open access PDFs.

### Example

`/parse-pdf?doi=10.1016/j.actaastro.2021.05.018`

Output:

```yaml
{
    "message": {
        "authors": [
            {
                "name": "Ahmedin Jemal",
                "affiliations": [
                    "Department of Epidemiol-ogy and Surveillance Research, Ameri-can Cancer Society, Atlanta, GA.",
                    "lance Information Services, De-partment of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Data Systems, Department of Epidemiology and Surveillance Re-search, American Cancer Society, Atlanta, GA.",
                    "Statistics Branch, Division of Vital Statistics, Centers for Disease Con-trol and Prevention, Hyattsville, MD.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "ment of Epidemiology and Surveil-lance Research, American Cancer Society, Atlanta, GA."
                ],
                "is_corresponding": false
            },
            {
                "name": "Rebecca Siegel",
                "affiliations": [
                    "Department of Epidemiol-ogy and Surveillance Research, Ameri-can Cancer Society, Atlanta, GA.",
                    "lance Information Services, De-partment of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Data Systems, Department of Epidemiology and Surveillance Re-search, American Cancer Society, Atlanta, GA.",
                    "Statistics Branch, Division of Vital Statistics, Centers for Disease Con-trol and Prevention, Hyattsville, MD.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "ment of Epidemiology and Surveil-lance Research, American Cancer Society, Atlanta, GA."
                ],
                "is_corresponding": false
            },
            {
                "name": "Elizabeth Ward",
                "affiliations": [
                    "Department of Epidemiol-ogy and Surveillance Research, Ameri-can Cancer Society, Atlanta, GA.",
                    "lance Information Services, De-partment of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Data Systems, Department of Epidemiology and Surveillance Re-search, American Cancer Society, Atlanta, GA.",
                    "Statistics Branch, Division of Vital Statistics, Centers for Disease Con-trol and Prevention, Hyattsville, MD.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "ment of Epidemiology and Surveil-lance Research, American Cancer Society, Atlanta, GA."
                ],
                "is_corresponding": false
            },
            {
                "name": "Taylor Murray",
                "affiliations": [
                    "Department of Epidemiol-ogy and Surveillance Research, Ameri-can Cancer Society, Atlanta, GA.",
                    "lance Information Services, De-partment of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Data Systems, Department of Epidemiology and Surveillance Re-search, American Cancer Society, Atlanta, GA.",
                    "Statistics Branch, Division of Vital Statistics, Centers for Disease Con-trol and Prevention, Hyattsville, MD.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "ment of Epidemiology and Surveil-lance Research, American Cancer Society, Atlanta, GA."
                ],
                "is_corresponding": false
            },
            {
                "name": "Jiaquan Xu",
                "affiliations": [
                    "Department of Epidemiol-ogy and Surveillance Research, Ameri-can Cancer Society, Atlanta, GA.",
                    "lance Information Services, De-partment of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Data Systems, Department of Epidemiology and Surveillance Re-search, American Cancer Society, Atlanta, GA.",
                    "Statistics Branch, Division of Vital Statistics, Centers for Disease Con-trol and Prevention, Hyattsville, MD.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "ment of Epidemiology and Surveil-lance Research, American Cancer Society, Atlanta, GA."
                ],
                "is_corresponding": false
            },
            {
                "name": "Carol Smigal",
                "affiliations": [
                    "Department of Epidemiol-ogy and Surveillance Research, Ameri-can Cancer Society, Atlanta, GA.",
                    "lance Information Services, De-partment of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Data Systems, Department of Epidemiology and Surveillance Re-search, American Cancer Society, Atlanta, GA.",
                    "Statistics Branch, Division of Vital Statistics, Centers for Disease Con-trol and Prevention, Hyattsville, MD.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "ment of Epidemiology and Surveil-lance Research, American Cancer Society, Atlanta, GA."
                ],
                "is_corresponding": false
            },
            {
                "name": "Michael Thun",
                "affiliations": [
                    "Department of Epidemiol-ogy and Surveillance Research, Ameri-can Cancer Society, Atlanta, GA.",
                    "lance Information Services, De-partment of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Data Systems, Department of Epidemiology and Surveillance Re-search, American Cancer Society, Atlanta, GA.",
                    "Statistics Branch, Division of Vital Statistics, Centers for Disease Con-trol and Prevention, Hyattsville, MD.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "ment of Epidemiology and Surveil-lance Research, American Cancer Society, Atlanta, GA."
                ],
                "is_corresponding": false
            },
            {
                "name": "Ms Siegel",
                "affiliations": [
                    "Department of Epidemiol-ogy and Surveillance Research, Ameri-can Cancer Society, Atlanta, GA.",
                    "lance Information Services, De-partment of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Data Systems, Department of Epidemiology and Surveillance Re-search, American Cancer Society, Atlanta, GA.",
                    "Statistics Branch, Division of Vital Statistics, Centers for Disease Con-trol and Prevention, Hyattsville, MD.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "ment of Epidemiology and Surveil-lance Research, American Cancer Society, Atlanta, GA."
                ],
                "is_corresponding": false
            },
            {
                "name": "Mr Murray",
                "affiliations": [
                    "Department of Epidemiol-ogy and Surveillance Research, Ameri-can Cancer Society, Atlanta, GA.",
                    "lance Information Services, De-partment of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Data Systems, Department of Epidemiology and Surveillance Re-search, American Cancer Society, Atlanta, GA.",
                    "Statistics Branch, Division of Vital Statistics, Centers for Disease Con-trol and Prevention, Hyattsville, MD.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "ment of Epidemiology and Surveil-lance Research, American Cancer Society, Atlanta, GA."
                ],
                "is_corresponding": false
            },
            {
                "name": "Mr Xu Is Epidemiologist",
                "affiliations": [
                    "Department of Epidemiol-ogy and Surveillance Research, Ameri-can Cancer Society, Atlanta, GA.",
                    "lance Information Services, De-partment of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Data Systems, Department of Epidemiology and Surveillance Re-search, American Cancer Society, Atlanta, GA.",
                    "Statistics Branch, Division of Vital Statistics, Centers for Disease Con-trol and Prevention, Hyattsville, MD.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "ment of Epidemiology and Surveil-lance Research, American Cancer Society, Atlanta, GA."
                ],
                "is_corresponding": false
            },
            {
                "name": "Ms Smigal Is Epidemiologist",
                "affiliations": [
                    "Department of Epidemiol-ogy and Surveillance Research, Ameri-can Cancer Society, Atlanta, GA.",
                    "lance Information Services, De-partment of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "Data Systems, Department of Epidemiology and Surveillance Re-search, American Cancer Society, Atlanta, GA.",
                    "Statistics Branch, Division of Vital Statistics, Centers for Disease Con-trol and Prevention, Hyattsville, MD.",
                    "Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA.",
                    "ment of Epidemiology and Surveil-lance Research, American Cancer Society, Atlanta, GA."
                ],
                "is_corresponding": false
            }
        ],
        "abstract": "Each year, the American Cancer Society estimates the number of new cancer cases and deaths expected in the United States in the current year and compiles the most recent data on cancer incidence, mortality, and survival based on incidence data from the National Cancer Institute and mortality data from the National Center for Health Statistics.Incidence and death rates are age-standardized to the 2000 US standard million population.A total of 1,399,790 new cancer cases and 564,830 deaths from cancer are expected in the United States in 2006.When deaths are aggregated by age, cancer has surpassed heart disease as the leading cause of death for those younger than age 85 since 1999.Delay-adjusted cancer incidence rates stabilized in men from 1995 through 2002, but continued to increase by 0.3% per year from 1987 through 2002 in women.Between 2002 and 2003, the actual number of recorded cancer deaths decreased by 778 in men, but increased by 409 in women, resulting in a net decrease of 369, the first decrease in the total number of cancer deaths since national mortality record keeping was instituted in 1930.The death rate from all cancers combined has decreased by 1.5% per year since 1993 among men and by 0.8% per year since 1992 among women.The mortality rate has also continued to decrease for the three most common cancer sites in men (lung and bronchus, colon and rectum, and prostate) and for breast and colon and rectum cancers in women.Lung cancer mortality among women continues to increase slightly.In analyses by race and ethnicity, African American men and women have 40% and 18% higher death rates from all cancers combined than White men and women, respectively.Cancer incidence and death rates are lower in other racial and ethnic groups than in Whites and African Americans for all sites combined and for the four major cancer sites.However, these groups generally have higher rates for stomach, liver, and cervical cancers than Whites.Furthermore, minority populations are more likely to be diagnosed with advanced stage disease than are Whites.Progress in reducing the burden of suffering and death from cancer can be accelerated by applying existing cancer control knowledge across all segments of the population.(CA",
        "fulltext": "Cancer Statistics, 2006          DVMAhmedinJemal   PhDRebeccaSiegel   MPHElizabethWard   PhDTaylorMurray   JiaquanXu   MPHCarolSmigal   MDMichaelJThun   MsSiegel   MrMurray   MortalityMrXu Is Epidemiologist   MsSmigal Is Epidemiologist    Department of Epidemiol-ogy and Surveillance Research, Ameri-can Cancer Society, Atlanta, GA. Department of Epidemiol-ogy and Surveillance Research Ameri-can Cancer Society  Atlanta GA      lance Information Services, De-partment of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA. lance Information Services De-partment of Epidemiology and Surveillance Research American Cancer Society  Atlanta GA      Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA. Department of Epidemiology and Surveillance Research American Cancer Society  Atlanta GA      Data Systems, Department of Epidemiology and Surveillance Re-search, American Cancer Society, Atlanta, GA. Data Systems Department of Epidemiology and Surveillance Re-search American Cancer Society  Atlanta GA      Statistics Branch, Division of Vital Statistics, Centers for Disease Con-trol and Prevention, Hyattsville, MD. Statistics Branch Division of Vital Statistics Centers for Disease Con-trol and Prevention  Hyattsville MD      Department of Epidemiology and Surveillance Research, American Cancer Society, Atlanta, GA. Department of Epidemiology and Surveillance Research American Cancer Society  Atlanta GA      ment of Epidemiology and Surveil-lance Research, American Cancer Society, Atlanta, GA. ment of Epidemiology and Surveil-lance Research American Cancer Society  Atlanta GA    Cancer Statistics, 2006       2432A23A94728E66CE4C66F8EAB7E309 10.3322/canjclin.56.2.106              Each year, the American Cancer Society estimates the number of new cancer cases and deaths expected in the United States in the current year and compiles the most recent data on cancer incidence, mortality, and survival based on incidence data from the National Cancer Institute and mortality data from the National Center for Health Statistics.Incidence and death rates are age-standardized to the 2000 US standard million population.A total of 1,399,790 new cancer cases and 564,830 deaths from cancer are expected in the United States in 2006.When deaths are aggregated by age, cancer has surpassed heart disease as the leading cause of death for those younger than age 85 since 1999.Delay-adjusted cancer incidence rates stabilized in men from 1995 through 2002, but continued to increase by 0.3% per year from 1987 through 2002 in women.Between 2002 and 2003, the actual number of recorded cancer deaths decreased by 778 in men, but increased by 409 in women, resulting in a net decrease of 369, the first decrease in the total number of cancer deaths since national mortality record keeping was instituted in 1930.The death rate from all cancers combined has decreased by 1.5% per year since 1993 among men and by 0.8% per year since 1992 among women.The mortality rate has also continued to decrease for the three most common cancer sites in men (lung and bronchus, colon and rectum, and prostate) and for breast and colon and rectum cancers in women.Lung cancer mortality among women continues to increase slightly.In analyses by race and ethnicity, African American men and women have 40% and 18% higher death rates from all cancers combined than White men and women, respectively.Cancer incidence and death rates are lower in other racial and ethnic groups than in Whites and African Americans for all sites combined and for the four major cancer sites.However, these groups generally have higher rates for stomach, liver, and cervical cancers than Whites.Furthermore, minority populations are more likely to be diagnosed with advanced stage disease than are Whites.Progress in reducing the burden of suffering and death from cancer can be accelerated by applying existing cancer control knowledge across all segments of the population.(CA     INTRODUCTIONCancer is a major public health problem in the United States and other developed countries.Currently, one in four deaths in the United States is due to cancer.In this article, we provide an overview of cancer statistics, including updated incidence, mortality, and survival rates and expected number of new cancer cases and deaths in 2006.3][4][5] State-specific incidence rates were abstracted from Cancer in North America (1998-2002) Volume One, based on data collected by cancer registries participating in the SEER program and Centers for Disease Control and Prevention (CDC)'s National Program of Cancer Registries.Population data were obtained from the US Census Bureau. 68][9] Cancer cases were classified according to the International Classification of Diseases for Oncology. 10 Estimated New Cancer CasesThe precise number of cancer cases diagnosed each year in the nation is unknown because complete cancer registration has not yet been achieved in many states.Consequently, for the national estimate  we first estimated the number of new cancer cases occurring annually in the United States from 1979 through 2002, using age-specific cancer incidence rates collected by the SEER program 2 and population data reported by the US Census Bureau. 6We then forecast the number of cancer cases expected to be diagnosed in the United States in the year 2006 using an autoregressive quadratic time-trend model fitted to the annual cancer case estimates. 11For estimates of new cancer cases in individual states, we projected the number of deaths from cancer in each state in 2006 and assumed that the ratio of estimated cancer deaths to cases in each state equaled that in the United States. Estimated Cancer DeathsWe used the state-space prediction method 12 to estimate the number of cancer deaths expected to occur in the United States and in each state in the year 2006.Projections arebased on underlying cause-of-death from death certificates as reported to the NCHS. 1 This model projects the number of cancer deaths expected to occur in 2006 based on the number that occurred each year from 1969 to 2003 in the United States and in each state separately. Other StatisticsWe provide mortality statistics for the leading causes of death as well as deaths from cancer in the year 2003.Causes of death for 2003 were coded and classified according to ICD-10. 7This report also provides updated statistics on trends in cancer incidence and mortality rates, the probability of developing cancer, and 5-year relative survival rates for selected cancer sites based on data from 1974 through 2002. 3All age-adjusted incidence and death rates are standardized to the 2000 US standard population and expressed per 100,000 population.The long-term incidence rates and trends (1975 to 2002) are adjusted for delays in reporting where possible.Delayed reporting affects the most recent 1 to 3 years of incidence data (in this case, 2000 to 2002), especially for cancers such as melanoma and prostate that are frequently diagnosed in outpatient settings.The NCI has developed a method to account for expected reporting delays in SEER registries for all cancer sites combined and several specific cancer sites when long-term incidence trends are analyzed. 13Delay-adjusted incidence provides a more accurate assessment of trends in the most recent years for which data are available.2. SELECTED FINDINGS Expected Numbers of New Cancer CasesFigure 1 indicates the most common cancers expected to occur in men and women in 2006.Among men, cancers of the prostate, lung and bronchus, and colon and rectum account for over 56% of all newly diagnosed cancer.Pros-  tate cancer alone accounts for about 33% (234,460) of incident cases in men.Based on cases diagnosed between 1995 and 2001, an estimated 91% of these new cases of prostate cancer are expected to be diagnosed at local or regional stages, for which 5-year relative survival approaches 100%.The three most commonly diagnosed cancers among women in 2006 will be cancers of the breast, lung and bronchus, and colon and rectum, accounting for about 54% of estimated cancer cases in women.Breast cancer alone is expected to account for 31% (212,920) of all new cancer cases among women. Expected Number of New Cancer DeathsTable 1 also shows the expected number of cancer deaths in 2006 for men, women, and both sexes combined.It is estimated that about 564,830 Americans will die from cancer, corresponding to over 1,500 deaths per day.Cancers of the lung and bronchus, colon and rectum, and prostate in men, and cancers of the lung and bronchus, breast, and colon and rectum in women continue to be the most common fatal cancers.These four cancers account for half of the total cancer deaths among men and women (Figure 1).Lung cancer surpassed breast cancer as the  3 provides the estimated number of cancer deaths in 2006 by state for selected cancer sites. Regional Variations in Cancer RatesTable 4 depicts cancer incidence for select cancers by state.Rates vary widely across states.For example, among the cancers listed in Table 4, the largest variation in the incidence rates (in proportionate terms) occurred in lung cancer in which rates (cases per 100,000 population) ranged from 42.3 in men and 21.5 in women in Utah to 138.2 in men and 72.3 in women in Kentucky.In contrast, the variation in female breast cancer incidence rates was small, ranging from 116.6 cases per 100,000 populations in New Mexico to 149.5 cases in Washington.Factors that contribute to the state variations in the incidence rates include differences in the prevalence of risk factors, access to and utilization of early detection services, and completeness of reporting.For example, the state variation in lung cancer incidence rates reflects differences in smoking prevalence; Utah ranks lowest in adult smoking prevalence and Kentucky highest.Figures 2 to 5 depict long-term trends in cancer incidence and death rates for all cancers combined and for selected cancer sites by sex.Table 5 shows incidence and mortality patterns for all cancer sites and for the four most common cancer sites based on joinpoint analysis.Trends in incidence were adjusted for delayed reporting.Delay-adjusted cancer incidence rates stabilized in men from 1995 to 2002 and increased in women by 0.3% per year from 1987 to 2002.Death rates for all cancer sites combined decreased by 1.5% per year from 1993 to 2002 in males and by 0.8% per year in females from 1992 to 2002.Mortality rates have continued to decrease across all four major cancer sites in men and in women, except for female lung cancer in which rates continued to increase by 0.3% per year from 1995 to 2002 (Table 5).The incidence trends are mixed, however.Lung cancer incidence rates are declining in men and have leveled off after increasing for many decades in women.The lag in the temporal trend of lung cancer incidence rates in women compared to men reflects historical differences in cigarette smoking between men and women; cigarette smoking in women peaked about 20 years later than in men.Colorectal cancer incidence rates have decreased from 1998 through 2002 in both males and in females.Prostate and female breast cancer incidence rates have continued to increase, although at a slower rate than in previous years.The continuing increase may be attributable to increased screening through prostate-specific antigen (PSA) testing for prostate cancer and mammography for breast cancer.Use of postmenopausal hormone therapy and increased prevalence of obesity may also be factors influencing the increase in female breast cancer incidence.Table 8 presents the number of deaths from all cancers combined and the five most common cancer sites for males and females at various ages.Among males under age 40, leukemia is the most common cause of cancer death, whereas cancer of the lung and bronchus predominates in men age 40 years and older.Colon and rectum and prostate cancer are the second most common causes of cancer death among men 40 to 79 years old and age 80 years and older, respectively.Among females, leukemia is the leading cause of cancer death before age 20, breast cancer ranks first at ages 20 to 59 years, and lung cancer ranks first at age 60 years and older.From 2002 to 2003, the number of recorded cancer deaths decreased by 778 in men, but increased by 409 in women (Table 9).The largest change in the total number of deaths from the major cancers was for prostate cancer in men (decreased by 892) and for lung cancer in women (increased by 575). CANCER OCCURRENCE BY RACE/ETHNICITYCancer incidence and death rates vary considerably among racial and ethnic groups (Table 10).For all cancer sites combined, African American men have a 23% higher incidence rate and 40% higher death rate than White men.African American women have a 7% lower inci- dence rate but an 18% higher death rate than White women for all cancer sites combined.For the specific cancer sites listed in Table 10, incidence and death rates are consistently higher in African Americans than in Whites, except for breast cancer (incidence) and lung cancer (mortality) among women.Death rates from prostate, stomach, and cervical cancers among African Americans are more than twice those in Whites.Factors known to contribute to racial disparities in mortality include differences in exposure (eg, Helicobacter pylori for stomach cancer), access to high-quality reg-ular screening (breast, cervical, and colorectal cancers), and timely treatment (for many cancers).The higher breast cancer incidence rate among Whites is thought to reflect a combination of factors that affect diagnosis, such as more frequent mammography in White women, and factors that affect disease risk, such as later age at first birth and greater use of hormone replacement therapy among White than African American women. 14mong other racial and ethnic groups, cancer incidence and death rates are lower for all cancer sites combined and for the four most common cancer sites than are rates in Whites and African Americans.However, incidence and death rates for cancers of the uterine cervix, stomach, and liver are generally higher in minority population than in Whites.Stomach and liver cancer incidence and death rates are more than twice as high in Asian/Pacific Islanders as in Whites, reflecting increased exposure to infectious agents such as H. pylori and Hepatitis B virus. 15 Trends in cancer incidence can only be adjusted for delayed reporting in Whites and African Americans, and not in other racial and ethnic subgroups because the long-term incidence data required for delay adjustment are available only for Whites and for African Americans.From 1992 to 2002, incidence rates for all cancer sites combined, not adjusted for delayed reporting, decreased by 2.7% per year among American Indians/Alaskan Natives, by 1.0% per year in African Americans, by 0.6% among Asian/Pacific Islanders, and by 0.4% among Hispanic-Latinos and Whites.Similarly, the death rate for all cancers combined decreased from 1992 through 2002 by 1.7% per year in Asian/Pacific Islanders, by 1.5% among African Americans, by 0.9% among Whites, and by 0.6% among Hispanic-Latinos.The death rate from all cancers combined stabilized during this time period among American Indians/Alaskan Natives. 3 Lifetime Probability of Developing CancerThe lifetime probability of developing cancer is higher for men (46%) than for women (38%) (Table 11).However, because of the relatively early age of onset of breast cancer, women have a slightly higher probability of developing cancer before the age of 60 years.It is noteworthy that these estimates are based on the average experience of the general population and may over or under estimate individual risk because of differences in exposure and/or genetic susceptibility. Cancer Survival by RaceCompared with Whites, African American men and women have poorer survival once a cancer diagnosis is made.As shown in Figure 7, African Americans are less likely than Whites to be diagnosed with cancer at a localized stage, when the disease may be more easily and successfully treated, and are more likely to be diagnosed with cancer at a regional or distant stage of disease.Five-year relative survival is lower in African Americans than Whites within each stratum of stage of diagnosis for nearly every cancer site (Figure 8).These disparities may result from inequalities in access to and receipt of quality health care and/or from dif-  ferences in comorbidities.The extent to which these factors, individually or collectively, contribute to the overall differential survival is unclear. 16However, recent findings suggest that African Americans who receive similar cancer treatment and medical care as Whites experience similar outcomes. 17here have been notable improvements over time in relative five-year survival rates for many cancer sites and for all cancers combined (Table 12).This is true for both Whites and African Americans.However, 5-year relative survival is still very poor (less than 25%) for many cancers, including pancreas, liver, esophagus, lung, and stomach.Relative survival rates cannot be calculated for other racial and ethnic populations because accurate life expectancies are not available.However, based on cause-specific survival rates of cancer patients diagnosed from 1992 to 2000 in SEER areas of the United States, all minority populations, except Asian/Pacific Islander women, have a greater probability of dying from cancer within 5 years of diagnosis than non-Hispanic Whites after accounting for dif-ferences in age at diagnosis. 18,19For the four major cancer sites (prostate, female breast, lung and bronchus, and colon and rectum), minority populations are more likely to be diagnosed at distant stage, compared with non-Hispanic Whites. 19 CANCER IN CHILDRENCancer is the second leading cause of death among children between the ages of 1 and 14 years in the United States; accidents are the most frequent cause of death in this age group (Table 13).The most common cancers in children (0 to 14 years) are leukemia (particularly acute lymphocytic leukemia), cancer of the brain and other nervous system, soft tissue sarcomas, non-Hodgkin Lymphoma, and renal (Wilms) tumors. 3Over the past 25 years, there have been significant improvements in the 5-year relative survival rate for many childhood cancers (Table 14).The 5-year relative survival rate among children for all cancer sites combined improved from *The distribution for localized stage represents localized and regional stages combined.Note: Staging according to Surveillance, Epidemiology, and End Results (SEER) historic stage categories rather than the American Joint Committee on Cancer (AJCC) staging system.For each type and race, stage categories do not total 100% because sufficient information is not available to assign a stage to all cancer cases.Source: Ries LAG, Eisner MP, Kosary Cl. et al.  \u2020The rate for localized stage represents localized and regional stages combined.Note: Staging according to Surveillance, Epidemiology, and End Results (SEER) historic stage categories rather than the American Joint Committee on Cancer (AJCC) staging system.Source: Ries LAG, Eisner MP, Kosary Cl, et al. CANCER AROUND THE WORLDTable 15 provides cancer death rates for 50 selected countries around the world for all sites combined and for 9 major sites, by sex.The highest lung cancer death rates are found in Hungary for men and in Denmark for women.China has the highest mortality rate for liver cancer in both men and women, reflecting the high prevalence of Hepatitis B virus in that country.The death rate for cervical cancer in Zimbabwe (43.1 per 100,000) is about 20 times that in the United States (2.3 per 100,000) and more than 25 times the rate in Australia (1.7 per 100,000). LIMITATIONS AND FUTURE CHALLENGESEstimates of the expected numbers of new cancer cases and cancer deaths should be interpreted cautiously.These estimates may vary considerably from year to year, particularly for less common cancers and in states with smaller populations.Unanticipated changes may occur that are not captured by our modeling efforts.The estimates of new cancer cases are based on incidence rates for the geographic locations that participate in the SEER program and, therefore, may not be representative of the entire United States.For these reasons, we discourage the use of these estimates to track year-to-year changes in cancer occurrence and death.Age-standardized or age-specific cancer death rates from the Na-tional Center for Health Statistics and cancer incidence rates from SEER are the preferred data sources for tracking cancer trends, even though these data are 3 and 4 years old, respectively, by the time that they become available.Despite their limitations, the American Cancer Society estimates of the number of new cancer cases and deaths in the current year provide reasonably accurate estimates of the burden of new cancer cases and deaths in the United States.Such estimates will assist in continuing efforts to reduce the public health burden of cancer., age-adjusted to the 2000 US standard population.Not all states submitted data for all years.\u2020This state's registry has submitted five years of data and passed rigorous criteria for each single year's data including: completeness of reporting, non-duplication of records, percent unknown in critical data fields, percent of cases registered with information from death certificates only, and internal consistency among data items.\u2021This state's registry did not submit incidence data to the North American Association of Central Cancer Registries (NAACCR) for 1998 to 2002.Source: Cancer in North America: 1998 to 2002, Volume One: Incidence, North American Association of Central Cancer Registries.CA Cancer J Clin 2006;56:106-130 Volume 56 Y Number 2 Y March/April 2006 111 FIGURE 33FIGURE 3 Annual Age-adjusted Cancer Incidence Rates* Among Males and Females for Selected Cancers, US, 1975 to 2002.*Rates are age-adjusted to the 2000 US standard population and adjusted for delays in reporting with the exception of melanoma.Source: Surveillance, Epidemiology, and End Results (SEER) program, nine oldest registries, 1975 to 2002, Division of Cancer Control and Population Sciences, National Cancer Institute, 2005. FIGURE 44FIGURE 4 Annual Age-adjusted Cancer Death Rates* Among Males for Selected Cancers, US, 1930 to 2002.*Rates are age-adjusted to the 2000 US standard population.Note: Due to changes in ICD coding, numerator information has changed over time.Rates for cancers of the lung and bronchus, colon and rectum, and liver are affected by these changes.Source: US Mortality Public Use Data Tapes, 1960 to 2002, US Mortality Volumes, 1930 to 1959, National Center for Health Statistics, Centers for Disease Control and Prevention, 2005. FIGURE 55FIGURE 5 Annual Age-adjusted Cancer Death Rates* Among Females for Selected Cancers, US, 1930 to 2002.*Rates are age-adjusted to the 2000 US standard population.Note: Due to changes in ICD coding, numerator information has changed over time.Rates for cancers of the uterus, ovary, lung and bronchus, and colon and rectum are affected by these changes.\u2020Uterus includes uterine cervix and uterine corpus.Source: US Mortality Public Use Data Tapes, 1960 to 2002, US Mortality Volumes 1930 to 1959, National Center for Health Statistics, Centers for Disease Control and Prevention, 2005. in the US in 2003, compared with 436,258 deaths from heart disease. FIGURE 66FIGURE 6 Death Rates* From Cancer and Heart Disease for Ages Younger than 85 and 85 and Older.*Rates are age-adjusted to the 2000 US standard population.Source: US Mortality Public Use Data Tapes, 1960 to 2002, National Center for Health Statistics, Centers for Disease Control and Prevention, 2005. Note: Effective with the mortality data for 1999, causes of death are classified by ICD-10, replacing ICD-9 used for 1979 to 1998 data.Source: US Mortality Public Use Data Tapes, 1989 to 2003, National Center for Health Statistics, Centers for Disease Control and Prevention, 2006. 33FIGURE 7 Distribution of Selected Cancers by Race and Stage at Diagnosis, US, 1995 to 2001.*The distribution for localized stage represents localized and regional stages combined.Note: Staging according to Surveillance, Epidemiology, and End Results (SEER) historic stage categories rather than the American Joint Committee on Cancer (AJCC) staging system.For each type and race, stage categories do not total 100% because sufficient information is not available to assign a stage to all cancer cases.Source: Ries LAG, Eisner MP, Kosary Cl. et al.3 FIGURE 88FIGURE 8 Five-year Relative Survival Rates Among Patients Diagnosed with Selected Cancers, by Race and Stage at Diagnosis, US, 1995 to 2001.*Data for distant stage melanoma of the skin for African American is not shown.\u2020Therate for localized stage represents localized and regional stages combined.Note: Staging according to Surveillance, Epidemiology, and End Results (SEER) historic stage categories rather than the American Joint Committee on Cancer (AJCC) staging system.Source: Ries LAG, Eisner MP, Kosary Cl, et al.3    TABLE 22Age-standardized Incidence Rates for All Cancers Combined, 1998-2002, and Estimated New Cases* for Selected Cancers by State, United States, 2006 *Rounded to the nearest 10; excludes basal and squamous cell skin cancers and in situ carcinomas except urinary bladder., 2006, 2, Downloaded from https://acsjournals.onlinelibrary.wiley.com/doi/10.3322/canjclin.56.2.106 by Readcube (Labtiva Inc.), Wiley Online Library on [28/06/2023].See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions)on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseCancer Statistics, 2006\u2020Average annual rates for 1998 -2002, age-adjusted to the 2000 US standard population; source: Cancer in North America; 1998 -2002, Vol.One: Incidence, NAACCR, based on data collected by cancer registries participating in NCI's SEER Program and CDC's National Program of Cancer Registries.\u2021Estimate is fewer than 50 cases.Note: These estimates are offered as a rough guide and should be interpreted with caution.State estimates are calculated according to the distribution of estimated cancer deaths in 2006 by state.State estimates may not add to US total due to rounding and exclusion of state estimates fewer than 50 cases.\u00a7Combined incidence rate is not available.\u00b6Incidence rate is for the Metropolitan Atlanta area.108 CA A Cancer Journal for Clinicians 15424863 TABLE 44Cancer Incidence Rates* by Site and State, US, 1998 to 2002*Per 100,000 Table 11invasive cancer does not include carcinomain situ of any site except urinary bladder, nordoes it include basal cell and squamous cellcancers of the skin. Over 1 million cases ofbasal cell and squamous cell skin cancer, about61,980 cases of breast carcinoma in situ, and49,710 cases of in situ melanoma are expectedto be newly diagnosed in 2006. The estimatednumbers of new cancer cases by state for se-lected cancer sites are shown in Tablepresents estimated numbers ofnew cancer cases expected among men andwomen in the United States in 2006. Theestimate of about 1.4 million new cases of , 2006, 2, Downloaded from https://acsjournals.onlinelibrary.wiley.com/doi/10.3322/canjclin.56.2.106 by Readcube (Labtiva Inc.), Wiley Online Library on [28/06/2023].See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions)on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License15424863Cancer Statistics, 2006114CA A Cancer Journal for Clinicians TABLE 55Trends in Cancer Incidence and Death Rates for Selected Cancers by Sex, US, 1975 to 2002Line Segment 1Line Segment 2Line Segment 3Line Segment 4YearAPC*YearAPC*YearAPC*YearAPC*All sites3APC, annual percent change based on rates age-adjusted to the 2000 standard population.\u2020TheAPC is significantly different from zero.Note: Trends were analyzed by Joinpoint Regression Program, version 3.0, with a maximum of three joinpoints (ie, four line segments).Trends in incidence are based on rates adjusted for delay in reporting.Source: Ries LAG, Eisner MP, Kosary CL, et al.3 14 Changes in the Recorded Number of Deaths from Cancer from 2002 to 2003 Atotal of 556,902 cancer deaths were recorded in the United States in 2003, the most recent year for which actual dates are available.About 369 fewer deaths were recorded in 2003 than in 2002, the first decrease since national mortality record keeping was instituted in 1930.Cancer accounted for about 23% of all deaths, ranking second only to heart disease (Table 6).When cause of death is ranked TABLE 66Fifteen Leading Causes of Death, United States, 2003 \u2020Rates are per 100,000 population and age-adjusted to the 2000 US standard population.Note: Percentages may not total 100 due to rounding.Symptoms, signs, and abnormalities, events of undetermined intent, and pneumonitis due to solids and liquids were excluded from the cause of death ranking order.Source: US Mortality Public Use Data Tape, 2003, National Center for Health Statistics, Centers for Disease Control and Prevention, 2006.CA Cancer J Clin 2006;56:106-130 Volume 56 Y Number 2 Y March/April 2006within each age group, categorized in 20-year age intervals, cancer is one of the five leading causes of death in each age group among both males and females (Table7).Cancer is the leading cause of death among women ages 40 to 79 and among men ages 60 to 79.When age-adjusted death rates are considered (Figure6), cancer is the leading cause of death among men and women under age 85.A total of 476,844 people under age 85 died from cancer TABLE 77Ten Leading Causes of Death by Age and Sex, United States, 2003 Note: Symptoms, signs, and abnormalities, events of undetermined intent, certain perinatal conditions, and pneumonitis due to solids and liquids were excluded from the cause of death ranking order.All ages excludes deaths with unknown age.Source: US Mortality Public Use Data Tapes, 2003, National Center for Health Statistics, Centers for Disease Control and Prevention, 2006. TABLE 88Reported Deaths for the Five Leading Cancer Sites by Age and Sex, United States, 2003 Other nervous system.Note: Others and Unspecified Primary excluded from cause of death ranking order.All ages excludes deaths with unknown age.Source: US Mortality Public Use Data Tapes, 2003, National Center for Health Statistics, Centers for Disease Control and Prevention, 2006.*ONS \u03ed TABLE 99Trends in the Recorded Number of Deaths for Selected Cancers by Sex, United States, 1989 to 2003CA Cancer J Clin 2006;56:106-130 TABLE 1010Age-standardized Incidence and Death Rates* for Selected Cancers by Race and Ethnicity, US, 1998 to 2002 Downloaded from https://acsjournals.onlinelibrary.wiley.com/doi/10.3322/canjclin.56.2.106 by Readcube (Labtiva Inc.), Wiley Online Library on [28/06/2023].See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions)on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseCancer Statistics, 200615424863, 2006, 2,AsianAmericanAmerican/Indian/AllAfricanPacificAlaskanHispanic-RacesWhiteAmericanIslanderNativeLatino \u2020Incidence RatesAll sitesMale553.3556.4682.6383.5255.4420.7Female413.5429.3398.5303.6220.5310.9Breast (Female)134.4141.1119.496.654.889.9Colon & rectumMale62.161.772.556.036.748.3Female46.045.356.039.732.232.3Lung & bronchusMale77.876.7113.959.442.644.6Female48.951.155.228.323.623.3Prostate173.8169.0272.0101.450.3141.9StomachMale12.310.717.721.015.917.2Female6.15.09.612.09.110.1Liver & bile ductMale9.37.412.121.48.714.1Female3.62.93.77.95.26.1Uterine cervix8.98.711.18.94.915.8Death RatesAll sitesMale247.5242.5339.4148.0159.7171.4Female165.5164.5194.399.4113.8111.0Breast (Female)26.425.934.712.713.816.7Colon & rectumMale24.824.334.015.816.217.7Female17.416.824.110.611.811.6Lung & bronchusMale76.375.2101.339.447.038.7Female40.941.839.918.827.114.8Prostate30.327.768.112.118.323.0StomachMale6.35.612.811.27.39.5Female3.22.86.36.84.15.3Liver & bile ductMale6.86.29.515.47.910.7Female3.02.73.86.54.35.1Uterine cervix2.82.55.32.72.63.5*Rates are per 100,000 and age-adjusted to the 2000 US standard population.\u2020Hispanics-Latinos are not mutually exclusive from Whites, African Americans, Asian Americans/Pacific Islanders, andAmerican Indians/Alaskan Natives.Source: Ries LAG, Eisner MP, Kosary CL, et al. 3122CA A Cancer Journal for Clinicians TABLE 1111Probability of Developing Invasive Cancers Within Selected Age Intervals, by Sex, US, 2000 to 2002*FIGURE 7 Distribution of Selected Cancers by Race and Stage at Diagnosis, US, 1995 to 2001. , 2006, 2, Downloaded from https://acsjournals.onlinelibrary.wiley.com/doi/10.3322/canjclin.56.2.106 by Readcube (Labtiva Inc.), Wiley Online Library on [28/06/2023].See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions)on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License 56% for patients diagnosed in 1974 to 1976 to 79% for those diagnosed in 1995 to 2001. 3CA Cancer J Clin 2006;56:106-130 Volume 56 Y Number 2 Y March/April 2006 125 15424863 TABLE 1212Trends in Five-year Relative Survival Rates* (%) for Selected Cancers by Race and Year of Diagnosis, US, 1974 to 2001.Relative Five-year Survival Rate (%)WhiteAfrican AmericanAll Races197419831995197419831995197419831995tototototototototoSite197619852001197619852001197619852001 15424863, 2006, 2, Downloaded from https://acsjournals.onlinelibrary.wiley.com/doi/10.3322/canjclin.56.2.106 by Readcube (Labtiva Inc.), Wiley Online Library on [28/06/2023].See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions)on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License   data from 1930 to 2003 in the United States were obtained from         Surveillance, Epidemiology, and End Results (SEER) Program (www.seer.cancer.gov) SEER*Stat Database: Incidence-SEER 9 Regs Public-Use, Nov 2004 Sub  1973-2002. April 2005   National Cancer Institute, DCCPS, Surveillance Research Program, Cancer Statistics Branch   based on the November 2004 submission Surveillance, Epidemiology, and End Re- sults (SEER) Program (www.seer.cancer.gov) SEER*Stat Database: Incidence-SEER 9 Regs Public-Use, Nov 2004 Sub (1973-2002), National Cancer Institute, DCCPS, Surveil- lance Research Program, Cancer Statistics Branch, released April 2005, based on the No- vember 2004 submission.     SEER Cancer Statistics Review, 1975-2002  LagRies   MPEisner   CLKosary  Bethesda, MD  National Cancer Institute   Ries LAG, Eisner MP, Kosary CL, et al. (eds). SEER Cancer Statistics Review, 1975- 2002. Bethesda, MD: National Cancer Insti- tute. Available at: http://seer.cancer. gov/csr/1975_2002/.    Surveillance, Epidemiology, and End Results (SEER) Program (www.seer.cancer.gov) SEER*Stat Database: Incidence-SEER 12 Regs Public-Use, Nov 2004 Sub for Expanded Races  1992-2002. April 2005   National Cancer Institute, DCCPS, Surveillance Research Program, Cancer Statistics Branch   based on the November 2004 submission Surveillance, Epidemiology, and End Results (SEER) Program (www.seer.cancer.gov) SEER*Stat Database: Incidence-SEER 12 Regs Public-Use, Nov 2004 Sub for Expanded Races (1992-2002), National Cancer Institute, DCCPS, Surveillance Research Program, Cancer Statistics Branch, released April 2005, based on the Novem- ber 2004 submission.    Surveillance, Epidemiology, and End Results (SEER) Program (www.seer.cancer.gov) SEER*Stat Database: Incidence-SEER 11 Regs Public-Use, Nov 2004 Sub for Hispanics  1992-2002. April 2005   National Cancer Institute, DC-CPS, Surveillance Research Program, Cancer Statistics Branch   based on the November 2004 submission Surveillance, Epidemiology, and End Re- sults (SEER) Program (www.seer.cancer.gov) SEER*Stat Database: Incidence-SEER 11 Regs Public-Use, Nov 2004 Sub for Hispanics (1992-2002), National Cancer Institute, DC- CPS, Surveillance Research Program, Cancer Statistics Branch, released April 2005, based on the November 2004 submission.       International Statistical Classification of Diseases, Injuries, and Causes of Death  1 10 1992 WHO Geneva   World Health Organization World Health Organization. International Statis- tical Classification of Diseases, Injuries, and Causes of Death. Vol. 1, 10th Rev. Geneva: WHO, 1992.       International Statistical Classification of Diseases, Injuries, and Causes of Death  1 9 1975 WHO Geneva   World Health Organization World Health Organization. International Statis- tical Classification of Diseases, Injuries, and Causes of Death. Vol. 1, 9th Rev. Geneva: WHO, 1975.       International Statistical Classification of Diseases, Injuries, and Causes of Death  1 8 1967 WHO Geneva   World Health Organization World Health Organization. International Statis- tical Classification of Diseases, Injuries, and Causes of Death. Vol. 1, 8th Rev. Geneva: WHO, 1967.    International Classification of Diseases for Oncology, 3rd Ed  AFritz   CPercy   AJack  Geneva  World Health Organization 2000   Fritz A, Percy C, Jack A, et al (eds.). Inter- national Classification of Diseases for Oncology, 3rd Ed. Geneva: World Health Organization, 2000.    Using cancer registry and vital statistics data to estimate the number of new cancer cases and deaths in the US for the upcoming year  PAWingo   SLandis   SParker    J Reg Management  25  1998   Wingo PA, Landis S, Parker S, et al. Using cancer registry and vital statistics data to estimate the number of new cancer cases and deaths in the US for the upcoming year. J Reg Management 1998;25:43-51.    A new method of predicting US and state-level cancer mortality counts for the current calendar year  RCTiwari   KGhosh   AJemal    CA Cancer J Clin  54  2004   Tiwari RC, Ghosh K, Jemal A, et al. A new method of predicting US and state-level cancer mortality counts for the current calendar year. CA Cancer J Clin 2004;54:30-40.    Impact of reporting delay and reporting error on cancer incidence rates and trends  LXClegg   EJFeuer   DNMidthune    J Natl Cancer Inst  94 1537 2002   Clegg LX, Feuer EJ, Midthune DN, et al. Impact of reporting delay and reporting error on cancer incidence rates and trends. J Natl Cancer Inst 2002;94:1537.    Trends in breast cancer by race and ethnicity  AGhafoor   AJemal   EWard    CA Cancer J Clin  53  2003   Ghafoor A, Jemal A, Ward E, et al. Trends in breast cancer by race and ethnicity. CA Cancer J Clin 2003;53:342-355.    Cancer Disparities by race/ethnicity and socioeconomic status  EWard   AJemal   VCokkinides    CA Cancer J Clin  54    Ward E, Jemal A, Cokkinides V, et al. Cancer Disparities by race/ethnicity and socio- economic status. CA Cancer J Clin 54:78-93.    Cancer statistics for African Americans  AGhafoor   AJemal   VCokkinides    CA Cancer J Clin  52  2002   Ghafoor A, Jemal A, Cokkinides V, et al. Cancer statistics for African Americans. CA Cancer J Clin 2002;52:326-341.    Survival of Blacks and Whites After a Cancer Diagnosis  PBBach   DSchrag   OWBrawley    JAMA  287  2002   Bach PB, Schrag D, Brawley OW, et al. Survival of Blacks and Whites After a Cancer Diagnosis. JAMA 2002;287:2106-2112.    Annual Report to the Nation on the status of cancer, 1975-2001, with a special feature regarding survival  AJemal   LXClegg   EWard    Cancer  101  2004   Jemal A, Clegg LX, Ward E, et al. Annual Report to the Nation on the status of cancer, 1975-2001, with a special feature regarding sur- vival. Cancer 2004;101:3-27.    Cancer survival among US whites and minorities: a SEER (Surveillance, Epidemiology, and End Results) Program population-based study  LXClegg   FPLi   BFHankey    Arch Intern Med  162  2002   Clegg LX, Li FP, Hankey BF, et al. Cancer survival among US whites and minorities: a SEER (Surveillance, Epidemiology, and End Re- sults) Program population-based study. Arch In- tern Med 2002;162:1985-1993.",
        "references": [
            {
                "doi": null,
                "title": "Surveillance, Epidemiology, and End Results (SEER) Program (www.seer.cancer.gov) SEER*Stat Database: Incidence-SEER 9 Regs Public-Use, Nov 2004 Sub",
                "author": null,
                "volume": null,
                "year": "1973-2002. April 2005",
                "journal": null,
                "page": null,
                "raw": "Surveillance, Epidemiology, and End Re- sults (SEER) Program (www.seer.cancer.gov) SEER*Stat Database: Incidence-SEER 9 Regs Public-Use, Nov 2004 Sub (1973-2002), National Cancer Institute, DCCPS, Surveil- lance Research Program, Cancer Statistics Branch, released April 2005, based on the No- vember 2004 submission."
            },
            {
                "doi": null,
                "title": "SEER Cancer Statistics Review, 1975-2002",
                "author": null,
                "volume": null,
                "year": null,
                "journal": null,
                "page": null,
                "raw": "Ries LAG, Eisner MP, Kosary CL, et al. (eds). SEER Cancer Statistics Review, 1975- 2002. Bethesda, MD: National Cancer Insti- tute. Available at: http://seer.cancer. gov/csr/1975_2002/."
            },
            {
                "doi": null,
                "title": "Surveillance, Epidemiology, and End Results (SEER) Program (www.seer.cancer.gov) SEER*Stat Database: Incidence-SEER 12 Regs Public-Use, Nov 2004 Sub for Expanded Races",
                "author": null,
                "volume": null,
                "year": "1992-2002. April 2005",
                "journal": null,
                "page": null,
                "raw": "Surveillance, Epidemiology, and End Results (SEER) Program (www.seer.cancer.gov) SEER*Stat Database: Incidence-SEER 12 Regs Public-Use, Nov 2004 Sub for Expanded Races (1992-2002), National Cancer Institute, DCCPS, Surveillance Research Program, Cancer Statistics Branch, released April 2005, based on the Novem- ber 2004 submission."
            },
            {
                "doi": null,
                "title": "Surveillance, Epidemiology, and End Results (SEER) Program (www.seer.cancer.gov) SEER*Stat Database: Incidence-SEER 11 Regs Public-Use, Nov 2004 Sub for Hispanics",
                "author": null,
                "volume": null,
                "year": "1992-2002. April 2005",
                "journal": null,
                "page": null,
                "raw": "Surveillance, Epidemiology, and End Re- sults (SEER) Program (www.seer.cancer.gov) SEER*Stat Database: Incidence-SEER 11 Regs Public-Use, Nov 2004 Sub for Hispanics (1992-2002), National Cancer Institute, DC- CPS, Surveillance Research Program, Cancer Statistics Branch, released April 2005, based on the November 2004 submission."
            },
            {
                "doi": null,
                "title": "",
                "author": null,
                "volume": "1",
                "year": "1992",
                "journal": "International Statistical Classification of Diseases, Injuries, and Causes of Death",
                "page": null,
                "raw": "World Health Organization. International Statis- tical Classification of Diseases, Injuries, and Causes of Death. Vol. 1, 10th Rev. Geneva: WHO, 1992."
            },
            {
                "doi": null,
                "title": "",
                "author": null,
                "volume": "1",
                "year": "1975",
                "journal": "International Statistical Classification of Diseases, Injuries, and Causes of Death",
                "page": null,
                "raw": "World Health Organization. International Statis- tical Classification of Diseases, Injuries, and Causes of Death. Vol. 1, 9th Rev. Geneva: WHO, 1975."
            },
            {
                "doi": null,
                "title": "",
                "author": null,
                "volume": "1",
                "year": "1967",
                "journal": "International Statistical Classification of Diseases, Injuries, and Causes of Death",
                "page": null,
                "raw": "World Health Organization. International Statis- tical Classification of Diseases, Injuries, and Causes of Death. Vol. 1, 8th Rev. Geneva: WHO, 1967."
            },
            {
                "doi": null,
                "title": "International Classification of Diseases for Oncology, 3rd Ed",
                "author": null,
                "volume": null,
                "year": "2000",
                "journal": null,
                "page": null,
                "raw": "Fritz A, Percy C, Jack A, et al (eds.). Inter- national Classification of Diseases for Oncology, 3rd Ed. Geneva: World Health Organization, 2000."
            },
            {
                "doi": null,
                "title": "Using cancer registry and vital statistics data to estimate the number of new cancer cases and deaths in the US for the upcoming year",
                "author": "P A Wingo",
                "volume": "25",
                "year": "1998",
                "journal": "J Reg Management",
                "page": "43 - 51",
                "raw": "Wingo PA, Landis S, Parker S, et al. Using cancer registry and vital statistics data to estimate the number of new cancer cases and deaths in the US for the upcoming year. J Reg Management 1998;25:43-51."
            },
            {
                "doi": null,
                "title": "A new method of predicting US and state-level cancer mortality counts for the current calendar year",
                "author": "R C Tiwari",
                "volume": "54",
                "year": "2004",
                "journal": "CA Cancer J Clin",
                "page": "30 - 40",
                "raw": "Tiwari RC, Ghosh K, Jemal A, et al. A new method of predicting US and state-level cancer mortality counts for the current calendar year. CA Cancer J Clin 2004;54:30-40."
            },
            {
                "doi": null,
                "title": "Impact of reporting delay and reporting error on cancer incidence rates and trends",
                "author": "L X Clegg",
                "volume": "94",
                "year": "2002",
                "journal": "J Natl Cancer Inst",
                "page": null,
                "raw": "Clegg LX, Feuer EJ, Midthune DN, et al. Impact of reporting delay and reporting error on cancer incidence rates and trends. J Natl Cancer Inst 2002;94:1537."
            },
            {
                "doi": null,
                "title": "Trends in breast cancer by race and ethnicity",
                "author": "A Ghafoor",
                "volume": "53",
                "year": "2003",
                "journal": "CA Cancer J Clin",
                "page": "342 - 355",
                "raw": "Ghafoor A, Jemal A, Ward E, et al. Trends in breast cancer by race and ethnicity. CA Cancer J Clin 2003;53:342-355."
            },
            {
                "doi": null,
                "title": "Cancer Disparities by race/ethnicity and socioeconomic status",
                "author": "E Ward",
                "volume": "54",
                "year": null,
                "journal": "CA Cancer J Clin",
                "page": "78 - 93",
                "raw": "Ward E, Jemal A, Cokkinides V, et al. Cancer Disparities by race/ethnicity and socio- economic status. CA Cancer J Clin 54:78-93."
            },
            {
                "doi": null,
                "title": "Cancer statistics for African Americans",
                "author": "A Ghafoor",
                "volume": "52",
                "year": "2002",
                "journal": "CA Cancer J Clin",
                "page": "326 - 341",
                "raw": "Ghafoor A, Jemal A, Cokkinides V, et al. Cancer statistics for African Americans. CA Cancer J Clin 2002;52:326-341."
            },
            {
                "doi": null,
                "title": "Survival of Blacks and Whites After a Cancer Diagnosis",
                "author": "P B Bach",
                "volume": "287",
                "year": "2002",
                "journal": "JAMA",
                "page": "2106 - 2112",
                "raw": "Bach PB, Schrag D, Brawley OW, et al. Survival of Blacks and Whites After a Cancer Diagnosis. JAMA 2002;287:2106-2112."
            },
            {
                "doi": null,
                "title": "Annual Report to the Nation on the status of cancer, 1975-2001, with a special feature regarding survival",
                "author": "A X Jemal",
                "volume": "101",
                "year": "2004",
                "journal": "Cancer",
                "page": "3 - 27",
                "raw": "Jemal A, Clegg LX, Ward E, et al. Annual Report to the Nation on the status of cancer, 1975-2001, with a special feature regarding sur- vival. Cancer 2004;101:3-27."
            },
            {
                "doi": null,
                "title": "Cancer survival among US whites and minorities: a SEER (Surveillance, Epidemiology, and End Results) Program population-based study",
                "author": "L X Clegg",
                "volume": "162",
                "year": "2002",
                "journal": "Arch Intern Med",
                "page": "1985 - 1993",
                "raw": "Clegg LX, Li FP, Hankey BF, et al. Cancer survival among US whites and minorities: a SEER (Surveillance, Epidemiology, and End Re- sults) Program population-based study. Arch In- tern Med 2002;162:1985-1993."
            }
        ]
    },
    "metadata": {
        "parser": "grobid",
        "doi": "10.3322/canjclin.56.2.106",
        "doi_url": "https://doi.org/10.3322/canjclin.56.2.106"
    }
}
```