��          �               �  5   �     �  s   �  j   d  �   �  F   �     �  
   �  e   �  _   ]  C   �  �     �  �  G   C  �   �  A   #  L   e  �   �  	   a	  ,   k	  �   �	  S   �
  �  �
  (   �  �  �  0   <     m  �   z  x      �   �  �   x          (  �   /  n   �  �   P  i  �  �  ?  >   �  �   :  <   �  <     �   B     0  *   7  �   b  C   4  ~  x  5   �   As you can see, this method requires four parameters: Display mode Here is an another style of navigation interface, and its corresponding example program is available at navigation. If you call NavigationInterface.setExpandWidth(), the large window width (1008px) will change accordingly. If you want to customize a navigation menu item, you should inherit the NavigationWidget and rewrite its paintEvent() and setCompacted()(optional). Here an example shows how to create an avatar item. Minimal display mode navigation interface is available at navigation3. More examples Navigation NavigationDisplayMode.COMPACT: A left, icon-only, nav panel on medium window widths (1007px or less). NavigationDisplayMode.EXPAND: An expanded left pane on large window widths (1008px or greater). NavigationDisplayMode.MENU: An expanded left menu (1007px or less). NavigationDisplayMode.MINIMAL: Only a menu button on small window widths (you should add and manage the menu button to main window by yourself like navigation3 does). NavigationInterface contains NavigationPanel which is used to place navigation menu items. All navigation menu items should inherit from NavigationWidget and you can add them to the panel by calling NavigationInterface.addWidget() or NavigationPanel.addWidget(). PyQt-Fluent-Widgets implements subclass NavigationPushButton and provides a convenient method NavigationInterface.addItem() to add it to the panel. NavigationItemPostion.BOTTOM: add widget to the bottom layout of panel. NavigationItemPostion.SCROLL: add widget to the scroll layout of panel. You can scroll the widgets in scroll layout when there are too many menu items. NavigationItemPostion.TOP: add widget to the top layout of panel. Now let's take a look at the parameters required for the addWidget() method: PyQt Fluent Widgets provides a side navigation class NavigationInterface. You can use it with QStackWidget and put them in QHBoxLayout. Examples are available at navigation2. Structure The navigation panel has four display modes: onClick: Slot function connected to the widget's clicked signal. If you want to switch sub interfaces when clicking widget, it is recommended to write this slot function as lambda: self.stackWidget.setCurrentWidget(self.xxxInterface) . position: Where to add the widget to the panel. The following values are available: routeKey: A unique name for the widget to be added. You can consider the sub interface in the QStackWidget as a web page, and the routeKey is the url of the web page. When you switch between sub interfaces, NavigationPanel will add a routeKey to the navigation history. When you click the return button, the routeKey at the top of the navigation history will pop up. If there are other routeKeys in the history at this time, PyQt-Fluent-Widgets will switch to the corresponding sub interface corresponding to current top routeKey. Otherwise, it will switch to the sub interface corresponding to defaultRouteKey, so you should call NavigationInterface.setDefaultRouteKey() before running app. widget: The widget to be added to panel. Project-Id-Version: PyQt-Fluent-Widgets 
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2023-04-08 21:09+0800
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: zh_CN
Language-Team: zh_CN <LL@li.org>
Plural-Forms: nplurals=1; plural=0;
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.11.0
 可以看到，这个方法需要四个参数： 显示模式 下面是另外一种风格的导航界面，对应的示例程序为 [navigation](https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/master/examples/navigation)。 如果调用了 `NavigationInterface.setExpandWidth()`，上述的窗口宽度阈值（1008px）将相应进行调整。 如果希望自定义一个导航项，可以创建 `NavigationWidget` 的子类并实现它的 `paintEvent()` 和 `setCompacted()`（可选） 方法。下面是一个简单例子，展示了如何定义头像导航项： 迷你导航界面如下图所示，可以在 [navigation3](https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/master/examples/navigation3) 获取完整代码。 更多示例 导航 `NavigationDisplayMode.COMPACT`：只在导航面板上显示图标，所有导航项都处于折叠状态（当窗口宽度小于 1007px 时默认使用这种显示模式）。 `NavigationDisplayMode.EXPAND`：左侧面板完全展开（当窗口的宽度大于等于 1008px 时可用） `NavigationDisplayMode.MENU`：展开的导航菜单（当窗口窗口小于 1007px 并点击菜单按钮时使用此显示模式） `NavigationDisplayMode.MINIMAL`：只显示一个菜单按钮。在这种显示模式下，应该自己创建并管理菜单按钮和 `NavigationPanel`，然后将菜单按钮的点击信号连接到 `NavigationPanel.toggle()` 函数上，具体写法可以参见 [navigation3](https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/master/examples/navigation3)。 `NavigationInterface` 内部使用 `NavigationPanel` 来放置导航菜单项。所有导航菜单项都需要继承自 `NavigationWidget`，可以调用 `NavigationInterface.addWidget()` 或者 `NavigationPanel.addWidget()` 将导航项添加到导航界面中。PyQt-Fluent-Widgets 实现了子类 `NavigationPushButton` ，同时提供了一个便捷的方法 `NavigationInterface.addItem()` 来创建导航项并将其到导航界面上。 `NavigationItemPostion.BOTTOM`: 添加到导航面板的底部 `NavigationItemPostion.SCROLL`：添加到导航面板的滚动区域。当导航菜单项太多时，滚动区域中导航项可以被滚动 `NavigationItemPostion.TOP`：添加到导航面板的顶部 现在让我们看看 `addWidget()` 方法的各个参数： PyQt-Fluent-Widgets 提供侧边导航类 `NavigationInterface`，可以将它和 `QStackWidget` 放在 `QHBoxLayout` 中。示例程序参见 [navigation2](https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/master/examples/navigation2) 结构 导航面板有以下四种显示模式： `onClick`：点击导航项时触发的槽函数。如果想在点击导航项时切换子界面，一种推荐的写法是将槽函数写作：`lambda: self.stackWidget.setCurrentWidget(self.xxxInterface)`。 `position`：导航项的位置。可以是下述值中的一种： `routeKey`：路由键，被添加到导航界面上的 `widget` 的唯一标识。如果将 `QStackWidget` 里面的子界面视为网页，`routeKey` 就是这个子界面的 URL。当用户切换子界面时，`NavigationPanel` 会将一个路由键添加到导航历史中。导航界面上的后退按钮被点击时，位于导航历史栈顶的路由键会被弹出，如果此时导航历史不为空，就可以切换到栈顶的路由键对应的子界面，否则就切换到 `defaultRouteKey` 对应的子界面，因此在运行 app 之前需要调用 `NavigationInterface.setDefaultRouteKey()` 设置一下默认子界面。 `widget`：被添加到导航界面上的导航项。 