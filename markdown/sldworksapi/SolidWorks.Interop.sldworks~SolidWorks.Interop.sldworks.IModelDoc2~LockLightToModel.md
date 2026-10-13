---
title: "LockLightToModel Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "LockLightToModel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LockLightToModel.html"
---

# LockLightToModel Method (IModelDoc2)

Locks or unlocks the specified light.

## Syntax

### Visual Basic (Declaration)

```vb
Function LockLightToModel( _
   ByVal LightId As System.Integer, _
   ByVal Fix As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim LightId As System.Integer
Dim Fix As System.Boolean
Dim value As System.Boolean

value = instance.LockLightToModel(LightId, Fix)
```

### C#

```csharp
System.bool LockLightToModel(
   System.int LightId,
   System.bool Fix
)
```

### C++/CLI

```cpp
System.bool LockLightToModel(
   System.int LightId,
   System.bool Fix
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LightId`: Light ID
- `Fix`: True if the light is locked, false if not

### Return Value

True if change is successful, false if not

## VBA Syntax

See [ModelDoc2::LockLightToModel](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~LockLightToModel.html).

## Examples

[Add Spotlight and Get Light Feature (C#)](Add_Spotlight_and_Get_Light_Feature_Example_CSharp.htm)
[Add Spotlight and Get Light Feature (VB.NET)](Add_Spotlight_and_Get_Light_Feature_Example_VBNET.htm)
[Add Spotlight and Get Light Feature (VBA)](Add_Spotlight_and_Get_Light_Feature_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IsLightLockedToModel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsLightLockedToModel.html)
[IModelDoc2::GetLightSourceIdFromName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceIdFromName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
