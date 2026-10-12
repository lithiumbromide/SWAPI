---
title: "SetMessage Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "SetMessage"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetMessage.html"
---

# SetMessage Method (IPropertyManagerPage2)

Obsolete. Superseded by [IPropertyManagerPage2::SetMessage2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~SetMessage2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMessage( _
   ByVal Message As System.String, _
   ByVal Visibility As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim Message As System.String
Dim Visibility As System.Integer
Dim value As System.Boolean

value = instance.SetMessage(Message, Visibility)
```

### C#

```csharp
System.bool SetMessage(
   System.string Message,
   System.int Visibility
)
```

### C++/CLI

```cpp
System.bool SetMessage(
   System.String^ Message,
   System.int Visibility
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Message`:
- `Visibility`:

## VBA Syntax

See [PropertyManagerPage2::SetMessage](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~SetMessage.html).

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)
