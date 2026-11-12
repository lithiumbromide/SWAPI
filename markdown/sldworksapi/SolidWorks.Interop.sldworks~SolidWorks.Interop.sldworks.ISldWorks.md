---
title: "ISldWorks Interface"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html"
---

# ISldWorks Interface

Provides direct and indirect access to all other interfaces exposed in the SOLIDWORKS API.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISldWorks
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
```

### C#

```csharp
public interface ISldWorks
```

### C++/CLI

```cpp
public interface class ISldWorks
```

## VBA Syntax

See [SldWorks](ms-its:sldworksapivb6.chm::/sldworks~SldWorks.html).

## Examples

[Get Spline Points (C++)](Get_Spline_Points_Example_CPlusPlus_COM.htm)
[Get Names of Creators of Features (C++)](Get_Names_of_Creators_of_Features_Examples_CPlusCPlus_COM.htm)
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Manage Drawing Document Line Styles (C#)](Manage_Drawing_Document_Line_Styles_Example_CSharp.htm)
[Manage Drawing Document Line Styles (VB.NET)](Manage_Drawing_Document_Line_Styles_Example_VBNET.htm)
[Manage Drawing Document Line Styles (VBA)](Manage_Drawing_Document_Line_Styles_Example_VB.htm)

## Remarks

This interface is the highest-level object in the SOLIDWORKS API. This interface provides a general set of functions that allow application-level operations such as create, open, close, and quit documents, arrange icons and windows, change the active document, and create attribute definitions.

Use CreateObject, GetObject, New, or similar functions to obtain the ISldWorks object from a Dispatch application (Visual Basic or C++ Dispatch). Standalone .exe C++ COM applications can use CoCreateInstance. All of the SOLIDWORKS API add-in wizards automatically create the ISldWorks object for you.

Events are implemented with delegates in the Microsoft .NET Framework. See the [Overview](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks_namespace.html) topic for a list of delegates for this interface.

## Access Diagram

[SldWorks](SWObjectModel.pdf#SldWorks)

## See Also

[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
