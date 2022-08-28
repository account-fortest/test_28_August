def key_values_nested_dictionary(dict_):

    def get_keys(dict_):
        for key, value in dict_.items():
            if isinstance(value, dict):
                yield (key)
                yield from get_keys(value)
            else:
                yield (key)


    def get_values(dict_):
        for value in dict_.values():
            if isinstance(value, dict):
                yield from get_values(value)
            else:
                yield value

    return (get_keys(dict_), get_values(dict_))


object1 = {"x":{"y":{"z":"a"}}}
object2 = {"a":{"b":{"c":"d"}}}

keys_, values_ = key_values_nested_dictionary(object1)

keys_list = []
for key in keys_:
    keys_list.append(key)

print ('keys = ', '/'.join(keys_list))
print ('value = ', ''.join(list(values_)))
