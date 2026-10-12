---
title: "LinkProperty Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "LinkProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~LinkProperty.html"
---

# LinkProperty Method (ICustomPropertyManager)

Sets whether to link or unlink the specified custom property to or from its parent part.

## Syntax

### Visual Basic (Declaration)

```vb
Function LinkProperty( _
   ByVal FieldName As System.String, _
   ByVal FieldLink As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim FieldLink As System.Boolean
Dim value As System.Integer

value = instance.LinkProperty(FieldName, FieldLink)
```

### C#

```csharp
System.int LinkProperty(
   System.string FieldName,
   System.bool FieldLink
)
```

### C++/CLI

```cpp
System.int LinkProperty(
   System.String^ FieldName,
   System.bool FieldLink
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`: Name of the custom property to link or unlink
- `FieldLink`: True to link the custom property, false to unlink it

### Return Value

Result code as defined in [swCustomLinkSetResult_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomLinkSetResult_e.html)

## VBA Syntax

See [CustomPropertyManager::LinkProperty](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~LinkProperty.html).

## Remarks

This method is valid for cut-list, feature, model, and configuration custom properties.

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomPropertyManager::LinkAll Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~LinkAll.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
