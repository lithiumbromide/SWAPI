---
title: "GetID Method (ILight)"
project: "SOLIDWORKS API Help"
interface: "ILight"
member: "GetID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILight~GetID.html"
---

# GetID Method (ILight)

Gets the light ID for this light feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetID() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILight
Dim value As System.Integer

value = instance.GetID()
```

### C#

```csharp
System.int GetID()
```

### C++/CLI

```cpp
System.int GetID();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Light ID for this light feature

## VBA Syntax

See [Light::GetID](ms-its:sldworksapivb6.chm::/sldworks~Light~GetID.html).

## Examples

[Redirect Spotlight (VBA)](Redirect_Spotlight_Example_VB.htm)
[Add Spotlight and Get Light Feature (C#)](Add_Spotlight_and_Get_Light_Feature_Example_CSharp.htm)
[Add Spotlight and Get Light Feature (VB.NET)](Add_Spotlight_and_Get_Light_Feature_Example_VBNET.htm)
[Add Spotlight and Get Light Feature (VBA)](Add_Spotlight_and_Get_Light_Feature_Example_VB.htm)

## Remarks

A light ID:

- is unique within the document.
- is persistent across SOLIDWORKS Design sessions and never changes, even if you change the name of the light.
- can be used to identify a specific light in a document.
- cannot be assigned by applications or users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm). You can get a light using its persistent reference ID, but you cannot get a light using this method.

## See Also

[ILight Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILight.html)
[ILight Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILight_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
