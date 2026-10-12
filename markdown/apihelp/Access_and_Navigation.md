---
title: "Access and Navigation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "apihelp/Access_and_Navigation.htm"
---

# Access and Navigation

#### Accessing API Help

Help is available on the Web or in your local installation directory. To enable your access to API Web Help, select SOLIDWORKS menu ? > Use Web Help. A check mark indicates that API Help is enabled and accessible on the Web.

To open context-sensitive SOLIDWORKS API Help from:

1. SOLIDWORKS VB.NET or C# macros opened in Visual Studio 2015:

  1. In the IDE, select **Help > Set Help Preference > Launch in Help Viewer**.
  2. Put your cursor on the interface, method, property, or delegate whose help topic you want displayed and press the F1 key.
2. SOLIDWORKS VB.NET or C# applications opened in Visual Studio 2012:

  1. In the IDE, put your cursor on the interface, method, property, or delegate whose help topic you want displayed and press the F1 key.
  2. If the associated help topic is not displayed, then select Tools > Options in the Help Viewer.

    1. Select Online.
    2. Select Try local first, then online or Try local only, not online.
    3. Select Local Help.
    4. Click OK.
    5. Put your cursor on the interface, method, property, or delegate in the IDE again and press F1.
3. SOLIDWORKS VBA macros:

  In the SOLIDWORKS Microsoft Visual Basic Integrated Developer Environment (IDE), put your cursor on the interface, method, property, or event whose help topic you want displayed and press the F1 key. The associated help topic is displayed.

IMPORTANT NAVIGATION CHANGES IN API HELP IN 2009 AND LATER

- Reference topics now use the name of the interface, not the object, as in earlier API Help systems.

  So, in this Help, it is:
- IAdvancedSelectionCriteria not AdvancedSelectionCriteria,
- IAnnotation not Annotation,
- IAnnotationView not AnnotationView,
- IAssemblyDoc not AssemblyDoc, etc.

All interface, method, properties, and delegate topics contain links to their corresponding Visual Basic for Applications (VBA) object, method, properties, and event topics. Additionally each Visual Basic for Applications (VBA) object topic includes that object's object model in graphical format, if an object model exists. If an object model does not exist, then the object's topic is blank.

- The SOLIDWORKS interfaces are no longer categorized by functionality on the Contents tab. Instead, they appear in alphabetical order in their respective interop assembly namespace book. If you prefer to locate SOLIDWORKS reference (i.e., interface, method, property, and delegate topics) topics categorized by functionality, then open the [Functional Categories](sldworksapi.chm::/SolidWorks.Interop.sldworks_Functionality.html) topic in the SOLIDWORKS APIs book, which is located in the SOLIDWORKS API Help book. The SolidWorks.Interop.sldworks Namespace book contains the majority of the reference topics for the SOLIDWORKS interfaces.

- Topics for obsolete interfaces, methods, properties, and delegates are not accessible from the Contents tab; however, they are accessible using the Index and Search tabs. Always read the description at the top of a topic. A link to the current version of a topic appears in the description. Descriptions for obsolete topics have intentionally been omitted.

#### Navigating API Help

NOTE: The following information applies to API Help when accessed locally only.

- ###### Index and Contents Tabs

If you are looking for specific functionality, but do not know the name of the function (interface, method, property, delegate, or enumerator), the quickest way to locate the function is to use the Index tab.

Index tab

Click the Index tab and type in the first few letters of the function whose topic you want displayed. For example to find the assembly interface topic, you can type assemb and Assemblies (see also IAssemblyDoc Interface) is selected. Double-click Assemblies (see also IAssemblyDoc Interface). Select IAssemblyDoc Interface and click Display in the Topics Found dialog.

Contents tab

You can also peruse the table of contents. Click the Contents tab, click a book to expand it, and examine its topics. API reference topics appear by product in their interop assembly namespace book or books.

All reference (interface, method, property, and delegate) topics include breadcrumbs near the top of the topic. These breadcrumbs can help you determine which product's topic you are reading. Additionally the name of a method's or property's interface appears enclosed in parentheses after the name of the method or property at the top of the topic and at the end of the breadcrumb.

- ###### Search Tab

If you cannot find the function that you want using the Index or Contents tabs, you can use the Search tab.

Type a word or phrase on the Search tab to see a list of topics that contain that word or phrase. For example, type tangent edges and click List Topics on the Search tab to see the topics that contain that exact or similar phrase. To reduce the number of topics found, clear the Match similar words (if selected) and select the Search titles only (if not selected) check boxes, which appear after the list. By default, the search results are ranked by number of occurrences of the word or phrase in the topic. You can alphabetize the search results by clicking Title.

You can also use wildcard expressions and boolean operations in your search word or phrase.

NOTE: If you specify an object by name in your search (e.g., Annotation), then the interface topic will appear in the search results (e.g., IAnnotation), not the object topic. Object topics do not appear in the search results; only the interface topics.

#### Wildcard Expressions (*, ?)

You can type the exact name of the function or you can use an * (asterisk) in your search expression to locate all of the topics that contain the search expression. For example, type noti* to locate all of the topics containing the word notify, notifies, notification, notice, and so on.

To locate all of the topics that contain just the word notify, type notif?. The ? (question mark) indicates to search for the specified expression string plus one character.

NOTE: The * and ? characters can appear at the beginning, embedded within, or at the end of a search expression. However, they cannot be the only character in the search expression.

Boolean Operators (AND, NEAR, NOT, OR)

You can use Boolean operators in the search expression. For example, if you are trying to find the SOLIDWORKS method that adds a mate condition between two assembly components, click the Search tab and type the following keywords and the Boolean operator AND:

assembly AND mate AND relationship

This search expression locates the IAssemblyDoc Interface Members, IAssemblyDoc Interface Methods, AddMate3 Method (IAssemblyDoc), EditMate2 Method (IAssemblyDoc), and, of course, this topic.

Other Boolean operators that you can use in your search string are:

- NEAR – Locate all of the topics that contain the specified terms, close together.
- NOT – Locate all of the topics that contain the term specified before NOT, then exclude all of the topics that contain the term specified after NOT
- OR – Locate all of the topics that contain any of the specified terms.
