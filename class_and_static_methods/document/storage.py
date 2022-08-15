from document.category import Category
from document.topic import Topic
from document.document import Document

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        found_category = self.__find_category(category.id)
        if found_category is None:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        found_topic = self.__find_topic(topic.id)
        if found_topic is None:
            self.topics.append(topic)

    def add_document(self, document: Document):
        found_document = self.__find_document(document.id)
        if found_document is None:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.__find_category(category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.__find_topic(topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = self.__find_document(document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__find_category(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__find_topic(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__find_document(document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.__find_document(document_id)
        return document

    def __repr__(self):
        return '\n'.join([repr(a) for a in self.documents])

    def __find_category(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                return category

    def __find_topic(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                return topic

    def __find_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document