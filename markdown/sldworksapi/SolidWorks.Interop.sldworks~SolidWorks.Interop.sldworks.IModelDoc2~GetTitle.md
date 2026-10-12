---
title: "GetTitle Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetTitle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetTitle.html"
---

# GetTitle Method (IModelDoc2)

Gets the title of the document that appears in the active window's title bar.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTitle() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.String

value = instance.GetTitle()
```

### C#

```csharp
System.string GetTitle()
```

### C++/CLI

```cpp
System.String^ GetTitle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Title string, usually displayed on the window's title bar

## VBA Syntax

See [ModelDoc2::GetTitle](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetTitle.html).

## Examples

[Detecting In-context Edit (C++)](Get_Edit_In_Context_Example_CPlusPlus_COM.htm)
[Close Document (VBA)](Close_Document_Example_VB.htm)
[Get Document Information (VBA)](Get_Document_Information_Example_VB.htm)
[Get Names of Components and Window Handle and DIBSECTION (VBA)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VB.htm)
[Get Names of Open Documents (VBA)](Get_Names_of_Open_Documents_Example_VB.htm)
[Save Rollbacked Part As Parasolid File (VBA)](Save_Roll_Backed_Part_as_Parasolid_File_Example_VB.htm)
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Get Names of Configurations Using Variant (C++)](ConfigurationTraversalCPP.htm)

## Remarks

The document name that appears in the window header changes based on your File Explorer settings. If you chose to suppress known file extensions, then the title shown in the window, and returned by this method, varies (for example, Part1.sldprt vs. Part1)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SetTitle2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetTitle2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
