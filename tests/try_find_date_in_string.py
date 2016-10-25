
import dateutil.parser
import logging
log = logging.getLogger(__name__)


def try_get_date_from_string_left_to_right(string):
    blocks = string.split()
    found_dates = []
    for block_index, block_value in enumerate(blocks):
        if block_index + 10 < len(blocks):
            end_index =  block_index + 10
        else:
            #~ end_index = len(blocks) - 1
            end_index = None

        block_string = " ".join([*blocks[block_index:end_index]])
        log.debug("block_string - (%s)", block_string)

        try:
            d = dateutil.parser.parse(block_string, fuzzy=True)
            found_dates.append(d)

            #~ date_string = ''
            #~ skip_to = 0
            #~ false_is_end = False
            #~ current_index = 0

            #~ while True:
                #~ try:
                    #~ t = dateutil.parser.parse(to_skip)
                    #~ false_is_end = True
                #~ except ValueError as ex:
                    #~ skip_to += 1

            log.debug("found_date - (%s)", d)



        except ValueError as ex:
            log.debug("not a date str(%s)", block_string)

    log.debug("string - (%s)", string)
    log.debug("founddates - (%s)", set([*found_dates]))

#~ def try_get_date_from_string_left_to_right(string):
    #~ blocks = string.split()
    #~ startblock = 0
    #~ founddates = []

    #~ while startblock < len(blocks) - 3:
        #~ tryblock = " ".join([*blocks[startblock:]])
        #~ try:
            #~ d = dateutil.parser.parse(tryblock, fuzzy=True)
            #~ log.info("is date : (%s) is a type(%s)", tryblock, type(d))

        #~ except Exception as ex:
            #~ log.debug("not a date : (%s)", tryblock)
        #~ startblock += 1


def try_get_date_from_string(string, *, method=">", interactive=False):
    methods = [">", "left_to_right", "<", "right_to_left"]
    if method in [">", "left_to_right"]:
        log.debug("method is (%s)", method)
        try_get_date_from_string_left_to_right(string)
    else:
        raise NotImplementedError("incorrect method")




if __name__ == "__main__":
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    fr = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(fr)
    log.addHandler(ch)

    import platform
    string = platform.uname().version
    string = "{} {}".format(string, "fuzzy data at end")
    string = "{} {}".format("fuzzy data at begining", string)
    string = "{} {}".format(string, "and another date 2012/01/02 13:45:52 UTC")

    try_get_date_from_string(string)
