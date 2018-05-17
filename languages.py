init_commands = { 'ru':{'task':u'Создать', 'list':u'Текущие задачи'},\
                  'en':{},}
task_commands = { 'ru':{'deadline':u'Срок', 'summary':u'Тема', 'priority':u'Приоритет', 'project':u'Тип'},\
                  'en':{},}
task_create_message = { 'ru':u'Опишите вашу проблему. Опционально, вы можете прикрепить файлы, указать тему задачи(краткое пояснение), \
желаемый срок исполнения, тип задачи и важность задачи',\
                        'en':''}
task_is_ready_message = {'ru':u'Задача готова к отправке, нажмите "Отправить", для отправки задачи. \
Предварительно, вы можете указать заголовок, срок, тип и важность задачи.',\
                         'en':''}
task_assignee_message = { 'ru':u'Кому вы хотите назначить задачу?',\
                          'en':''}
file_accepted_message = { 'ru':u'Файл будет добавлен к задаче.',\
                          'en':''}
file_type_error = { 'ru':u'Неизвестный тип файла.',\
                          'en':''}
inline_assignee_message = { 'ru':u'Вы назначаете задачу пользователю {0}',\
                            'en':'' }
no_task_error = {'ru':u'Чтобы прикрепить к задаче файл, нажмете "Создать", а потом отправляйте файл.',
                 'en':''}
task_summary_message = { 'ru':u'Вкратце опишите вашу проблему.',\
                         'en':''}
summary_was_set_message = {'ru':u'Вы указали тему (описание) вашей задачи. Если вы хотите поменять его, повторно нажмите на кнопку "Тема"',\
                           'en':''}
task_deadline_message = {'ru':u'Укажите желаемый срок выполнения задачи в днях',\
                         'en':''}
deadline_was_set_message = {'ru':u'Срок исполения задачи: {0} дней',\
                            'en':''}
priority_list = { 'ru': {u'Низкий':'Low',u'Средний':'Medium',u'Высокий':'High'},
                  'en': {'Low':'Low', 'Medium':'Medium', 'High':'High'} }
task_priority_message = {'ru':u'Выбирете приоритет задачи',\
                        'en':''}
priority_was_set_message = {'ru':u'Задача будет создана с приоритетом: {0}',\
                           'en':''}
task_project_message = {'ru':u'Выбирете тип задачи',\
                        'en':''}
project_was_set_message = {'ru':u'Вы выбрали тип задачи: {0}',\
                           'en':''}
project_error_message = {'ru':u'Вы выбрали некорректный тип задачи. Выберите тип из списка.',\
                         'en':''}
update_is_ok_message = {'ru':u'Изменения сохранены',\
                        'en':''}
no_text_message = {'ru':u'Вы не описали вашу задачу. Пожалуйста, отправьте мне(Боту) суть вашей проблемы и нажмите "-ОТПРАВИТЬ-"',\
                   'en':''}
error_message = { 'ru':u'что-то пошло не так! Убидитесь, что все данные введены в правильном формате и попробуйте повторить операцию.',\
                  'en':''}
hello_message = { 'ru':u'Чем обязаны?',\
                  'en':''}
task_was_created_error = { 'ru':u'Не возможно редактировать задачи после создания.', \
                           'en':u'' }
no_authorization_message = { 'ru':u'У вас недостаточно привилегий для данной операции. Обратитесь к администратору системы',\
                             'en':''}
task_was_created_message = { 'ru':u'Задача {0} отправлена пользователю {1}',\
                             'en':'' }
jirauser_assignee_list = { 'ru':u'Задачи назначенные на пользователя {0} ', \
                            'en':'' }
jirauser_author_list = { 'ru':u'Задачи от пользователя {0} ', \
                            'en':'' }

cancel_key = {'ru':u'-ОТМЕНА-',\
              'en':'-CANCEL-'}
send_task_key = {'ru':u'-ОТПРАВИТЬ-',\
                 'en':'-SEND-'}