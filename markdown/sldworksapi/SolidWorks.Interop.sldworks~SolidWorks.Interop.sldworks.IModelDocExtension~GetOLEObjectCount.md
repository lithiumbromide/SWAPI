---
title: "GetOLEObjectCount Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetOLEObjectCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjectCount.html"
---

# GetOLEObjectCount Method (IModelDocExtension)

Gets the number of OLE objects.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOLEObjectCount( _
   ByVal Options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Options As System.Integer
Dim value As System.Integer

value = instance.GetOLEObjectCount(Options)
```

### C#

```csharp
System.int GetOLEObjectCount(
   System.int Options
)
```

### C++/CLI

```cpp
System.int GetOLEObjectCount(
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: Options as defined in [swOleObjectOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swOleObjectOptions_e.html)

### Return Value

Number of OLE objects

## VBA Syntax

See [ModelDocExtension::GetOLEObjectCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetOLEObjectCount.html).

## Examples

[Determine if OLE Objects Are Linked or Embedded (VBA)](Determine_if_OLE_Objects_are_Linked_or_Embedded_Example_VB.htm)

## Remarks

Call this method before calling [IModelDocExtension::IGetOLEObjects](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetOLEObjects.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateOLEObject.html)
[IModelDocExtension::GetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjects.html)
[IModelDocExtension::ICreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ICreateOLEObject.html)
[IModelDocExtension::IGetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetOLEObjects.html)
[IModelDocExtension::InsertObjectFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertObjectFromFile.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
