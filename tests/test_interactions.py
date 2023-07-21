from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


class TestInteractions:

    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, 'Сортировка в LIST элементах не изменилась'
            assert grid_before != grid_after, 'Сортировка в GRID элементах не изменилась'

    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            active_el_list = selectable_page.select_list_item()
            active_el_grid = selectable_page.select_grid_item()
            assert len(active_el_list) != 0, 'Нет выбранных элементов LIST'
            assert len(active_el_grid) != 0, 'Нет выбранных элементов GRID'

    class TestResizablePage:

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_size, min_size = resizable_page.change_size_resizable()
            assert ('500px', '300px') == max_box, 'Максимальное значение больше 500 на 300'
            assert ('150px', '150px') == min_box, 'Минимальное значение меньше 150 на 150'
            assert max_size != min_size, 'Размер не менялся'

    class TestDroppablePage:

        def test_simple_page(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            drop_div_text = droppable_page.drop_simple()
            print(drop_div_text)
            assert drop_div_text == 'Dropped!', "Элемент не переместился в дроп зону"

        def test_accept_page(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_accept_text, accept_text = droppable_page.drop_accept()
            assert not_accept_text == 'Drop here', "Проблемы с элементом Not Acceptable"
            assert accept_text == 'Dropped!', "Проблемы с элементом Acceptable"

        def test_prevent_propogation_page(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box = droppable_page.drop_prevent_propgation()
            assert text_not_greedy_box == 'Dropped!', 'Элемент не перемещен'
            assert text_not_greedy_inner_box == 'Dropped!', "Всплытие события не работает"
            assert text_greedy_box == 'Outer droppable', "Произошло всплытие события"
            assert text_greedy_inner_box == 'Dropped!', "Элемент не перемещен"

        def test_revert_draggable_page(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will')
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will')
            assert will_after_move != will_after_revert, 'Элемент вернулся в исходную точку'
            assert not_will_after_move == not_will_after_revert, 'Элемент остался в drop div'

    class TestDraggablePage:

        def test_draggable_page(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            before_position, after_position = draggable_page.simple_drag_box()
            assert before_position != after_position, 'Элемент не был перемещен'

        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            top_x, left_x = draggable_page.axis_restricted_x()
            top_y, left_y = draggable_page.axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(
                top_x[1][0]) == 0, "box position has not changed or there has been a shift in the y-axis"
            assert left_x[0][0] != left_x[1][0] and int(
                left_x[1][0]) != 0, "box position has not changed or there has been a shift in the y-axis"
            assert top_y[0][0] != top_y[1][0] and int(
                top_y[1][0]) != 0, "box position has not changed or there has been a shift in the x-axis"
            assert left_y[0][0] == left_y[1][0] and int(
                left_y[1][0]) == 0, "box position has not changed or there has been a shift in the x-axis"



