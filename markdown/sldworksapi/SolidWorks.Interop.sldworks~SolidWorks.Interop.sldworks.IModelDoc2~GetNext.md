---
title: "GetNext Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetNext.html"
---

# GetNext Method (IModelDoc2)

Gets the next document opened in the current SOLIDWORKS Design session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Object

value = instance.GetNext()
```

### C#

```csharp
System.object GetNext()
```

### C++/CLI

```cpp
System.Object^ GetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) opened in the current SOLIDWORKS Design session

## VBA Syntax

See [ModelDoc2::GetNext](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetNext.html).

## Examples

[Determine If Document Is Dirty (VBA)](Determine_if_Document_is_Dirty_Example_VB.htm)
[Get Names of Open Documents (VBA)](Get_Names_of_Open_Documents_Example_VB.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (C#)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_CSharp.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (VB.NET)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VBNET.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (VBA)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VB.htm)

## Remarks

To traverse all documents open in this SOLIDWORKS Design session, [ISldWorks::GetFirstDocument](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetFirstDocument.html) must have returned the first IModleDoc2 object that calls this method.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetNext.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
