# Начните работу над проектом «Электронный файл исследования».
# Создайте класс, описывающий систему хранения электронных документов, а также класс «Документ»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы документов.
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа документов.
# Разработать методы, отвечающие за проверку и валидацию документов,
# а также файлирование документов в соответствующую папку в системе.
# Для хранения данных о наименовании и количестве документов, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

from abc import ABC, abstractmethod
from datetime import datetime


class MultiUploader:
    MFDL_list = {"Study A": [], "Study B": [], "Study C": []}


class TMF:
    def __init__(self, study_title):
        self.study_title = study_title
        self._structure = {"Central Trial Documents":
                     {"Subject Documentation": []},
                 "Regulatory":
                     {"Submission": [],
                      "Approval": [],
                      "Trial Status Reporting": []},
                 "Site Management":
                     {"Site Initiation":
                          {"Evidence of Training": []},
                      "Site Set-up":
                          {"CV": [], "Site Staff Qualification": []}}}

    @property
    def structure(self):
        return self._structure

    @staticmethod
    def pretty(d, indent=0):
        for key, value in d.items():
            print('\t' * indent + str(key))
            if isinstance(value, dict):
                TMF.pretty(value, indent + 1)
            else:
                print('\t' * (indent + 1) + str(value))


class Document:
    def __init__(self, name, date, quality, study, doc_type):
        self.name = name
        self.date = date
        self.quality = quality
        self.study = study
        self.doc_type = doc_type

    def __repr__(self):
        return self.name


class RADocs(Document):
    pass


class QualDocs(Document):
    def __init__(self, name, date, expiry, quality, study, doc_type):
        super().__init__(name, date, quality, study, doc_type)
        self.expiry = expiry


class PtMaterials(Document):
    pass


class Person(ABC):
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.last_name = last_name

    @abstractmethod
    def quality_check(self, doc, rejected_docs, need_ntf_docs):
        pass


class Adder(Person):
    def quality_check(self, doc, rejected_docs, need_ntf_docs):
        pass

    def add_doc(self, mfdl_list, doc_list):
        for doc in doc_list:
            a = mfdl_list.MFDL_list.get(doc.study)
            if a is None:
                print("Study not found")
            a.append(doc)
        return mfdl_list.MFDL_list


class Indexer(Person):
    @staticmethod
    def find_value_by_key(mydict, mykey):
        for key, value in mydict.items():
            if key == mykey:
                return value
            elif isinstance(value, dict):
                b = Indexer.find_value_by_key(value, mykey)
                if b is not None:
                    return b
        return None

    def quality_check(self, doc, rejected_docs, need_ntf_docs):
        if doc.quality < 3.0:
            print(f"{doc.name}: Document quality not acceptable, please provide replacement")
            rejected_docs.append(doc)
            return False
        elif 3.0 < doc.quality < 4.6:
            print(f"{doc.name}: Poor document quality, Note to File required")
            need_ntf_docs.append(doc)
            return False
        return True

    def index_doc(self, mydict, title, structure):
        rejected_docs = []
        need_ntf_docs = []
        for mylist in mydict.values():
            for doc in mylist:
                if title == doc.study:
                    if self.quality_check(doc, rejected_docs, need_ntf_docs) is True:
                        mykey = doc.doc_type
                        c = Indexer.find_value_by_key(structure, mykey)
                        if c is not None:
                            c.append(doc)

        return rejected_docs, need_ntf_docs


class FileReviewer(Person):
    def quality_check(self, doc, rejected_docs, need_ntf_docs):
        pass

    def do_file_review(self, structure):
        for mylist in structure.values():
            if isinstance(mylist, list):
                for doc in mylist:
                    doc_approved = True
                    try:
                        expiration = datetime.strptime(doc.expiry, "%d/%m/%Y")
                        present = datetime.now()
                        if expiration.date() < present.date():
                            doc_approved = False
                            print(f"{doc.name}: Document expired, please provide valid one")
                    except:
                        pass
                    if doc_approved is True:
                        print(f"{doc.name}: Document approved")
            elif isinstance(mylist, dict):
                self.do_file_review(mylist)


init_list = []

InformedConsent_1 = PtMaterials("Main_V1", "01/01/2021", 5.0, "Study A", "Subject Documentation")
init_list.append(InformedConsent_1)
InformedConsent_2 = PtMaterials("Parental_V1", "12/01/2021", 4.7, "Study B", "Subject Documentation")
init_list.append(InformedConsent_2)

Init_1 = RADocs("Initial Submission", "22/02/2019", 2.5, "Study A", "Submission")
init_list.append(Init_1)
Init_2 = RADocs("Initial Approval", "25/02/2019", 2.0, "Study A", "Approval")
init_list.append(Init_2)

Notif_1 = RADocs("IB V20", "12/03/2020", 4.9, "Study B", "Submission")
init_list.append(Notif_1)
Report_1 = RADocs("Annual Report 1", "23/03/2021", 4.8, "Study C", "Trial Status Reporting")
init_list.append(Report_1)

CV_1 = QualDocs("CV_PI", "12/07/2017", None, 5.0, "Study A", "CV")
init_list.append(CV_1)
CV_2 = QualDocs("CV_SI", "15/09/2018", None, 3.6, "Study A", "CV")
init_list.append(CV_2)
CV_3 = QualDocs("CV_SC", "02/08/2019", None, 1.3, "Study A", "CV")
init_list.append(CV_3)

GCP_1 = QualDocs("GCP_SI", "21/09/2017", "20/09/2020", 5.0, "Study A", "Site Staff Qualification")
init_list.append(GCP_1)
ML_1 = QualDocs("Medical License_PI", "01/01/2021", "31/12/2021", 4.6, "Study B", "Site Staff Qualification")
init_list.append(ML_1)
IATA_1 = QualDocs("IATA_SC", "11/04/2020", "11/04/2022", 4.7, "Study A", "Site Staff Qualification")
init_list.append(IATA_1)

Train_Cert_1 = QualDocs("EDC_PI", "22/10/2016", None, 4.9, "Study B", "Evidence of Training")
init_list.append(Train_Cert_1)
Train_Cert_2 = QualDocs("Protocol Training_SI", "28/11/2018", None, 4.8, "Study B", "Evidence of Training")
init_list.append(Train_Cert_2)

# print(init_list)

MFDL_1 = MultiUploader()

Adder_1 = Adder("Evgeny", "Ivanov")
print(Adder_1.add_doc(MFDL_1, init_list))

Study_1 = TMF("Study A")
Study_2 = TMF("Study B")
Study_3 = TMF("Study C")

Indexer_1 = Indexer("Tony", "Du")
res_tuple = Indexer_1.index_doc(MFDL_1.MFDL_list, Study_1.study_title, Study_1.structure)
print(f"Documents required workaround: {res_tuple[0]}")
print(f"Documents required NTF: {res_tuple[1]}")
TMF.pretty(Study_1.structure)

Indexer_2 = Indexer("Maggie", "Dade")
res_tuple = Indexer_2.index_doc(MFDL_1.MFDL_list, Study_2.study_title, Study_2.structure)
print(f"Documents required workaround: {res_tuple[0]}")
print(f"Documents required NTF: {res_tuple[1]}")
TMF.pretty(Study_2.structure)

Indexer_3 = Indexer("Terisa", "Tian")
res_tuple = Indexer_3.index_doc(MFDL_1.MFDL_list, Study_3.study_title, Study_3.structure)
print(f"Documents required workaround: {res_tuple[0]}")
print(f"Documents required NTF: {res_tuple[1]}")
TMF.pretty(Study_3.structure)

Reviewer_1 = FileReviewer("Nick", "Clark")
Reviewer_1.do_file_review(Study_1.structure)

Reviewer_2 = FileReviewer("Milena","Ivanova")
Reviewer_2.do_file_review(Study_2.structure)

Reviewer_3 = FileReviewer("Irene","Liu")
Reviewer_3.do_file_review(Study_3.structure)
