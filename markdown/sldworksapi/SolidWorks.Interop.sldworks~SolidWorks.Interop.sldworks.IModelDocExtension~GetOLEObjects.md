---
title: "GetOLEObjects Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetOLEObjects"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjects.html"
---

# GetOLEObjects Method (IModelDocExtension)

Get the OLE objects.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOLEObjects( _
   ByVal Options As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Options As System.Integer
Dim value As System.Object

value = instance.GetOLEObjects(Options)
```

### C#

```csharp
System.object GetOLEObjects(
   System.int Options
)
```

### C++/CLI

```cpp
System.Object^ GetOLEObjects(
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: Options as defined in [swOleObjectOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swOleObjectOptions_e.html)

### Return Value

Array of the [OLE objects](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject.html)

## VBA Syntax

See [ModelDocExtension::GetOLEObjects](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetOLEObjects.html).

## Examples

[Determine if OLE Objects Are Linked or Embedded (VBA)](Determine_if_OLE_Objects_are_Linked_or_Embedded_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateOLEObject.html)
[IModelDocExtension::GetOLEObjectCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjectCount.html)
[IModelDocExtension::ICreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ICreateOLEObject.html)
[IModelDocExtension::IGetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetOLEObjects.html)
[IModelDocExtension::InsertObjectFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertObjectFromFile.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
