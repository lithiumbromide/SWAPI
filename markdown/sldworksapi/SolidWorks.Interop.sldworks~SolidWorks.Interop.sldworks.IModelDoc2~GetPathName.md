---
title: "GetPathName Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetPathName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPathName.html"
---

# GetPathName Method (IModelDoc2)

Gets the full path name for this document, including the file name.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPathName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.String

value = instance.GetPathName()
```

### C#

```csharp
System.string GetPathName()
```

### C++/CLI

```cpp
System.String^ GetPathName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Full path name for this document including the file name; if the document has not yet been saved, then the string is empty

## VBA Syntax

See [ModelDoc2::GetPathName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetPathName.html).

## Examples

[Get List of Open Documents (C++)](Get_List_of_Open_Documents_Example_CPlusPlus_COM.htm)
[Find Total Length of Sketch Segments in Sketch (VBA)](Find_Total_Length_of_Sketch_Segments_in_Sketch_Example_VB.htm)
[Get Active Document Dependents (VBA)](Get_Active_Document_Dependents_Example_VB.htm)
[Get File Summary Information (VBA)](Get_File_Summary_Information_Example_VB.htm)
[Get Unopened Document Dependents (VBA)](Get_Unopened_Document_Dependents_Example_VB.htm)
[Get Paths of Open Documents (C#)](Get_Paths_of_Open_Documents_Example_CSharp.htm)
[Get Paths of Open Documents (VB.NET)](Get_Paths_of_Open_Documents_Example_VBNET.htm)
[Get Paths of Open Documents (VBA)](Get_Paths_of_Open_Documents_Example_VB.htm)
[Get List of Configurations (C#)](Get_List_Of_Configurations_Example_CSharp.htm)
[Get List of Configurations (VB.NET)](Get_List_Of_Configurations_Example_VBNET.htm)
[Get List of Configurations (VBA)](Get_List_Of_Configurations_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IComponent2::GetPathName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetPathName.html)
[IComponent2::GetImportedPath Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetImportedPath.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
