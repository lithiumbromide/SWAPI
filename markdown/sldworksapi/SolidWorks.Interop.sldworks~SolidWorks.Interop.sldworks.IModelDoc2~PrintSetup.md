---
title: "PrintSetup Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "PrintSetup"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintSetup.html"
---

# PrintSetup Property (IModelDoc2)

Obsolete. See [IModelDo2::SetUserPreferenceDoubleValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetUserPreferenceDoubleValue.html), [IModelDoc2::SetUserPreferenceIntegerValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetUserPreferenceIntegerValue.html), and [IModelDoc2::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property PrintSetup( _
   ByVal SetupType As System.Integer _
) As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim SetupType As System.Integer
Dim value As System.Short

instance.PrintSetup(SetupType) = value

value = instance.PrintSetup(SetupType)
```

### C#

```csharp
System.short PrintSetup(
   System.int SetupType
) {get; set;}
```

### C++/CLI

```cpp
property System.short PrintSetup {
   System.short get(System.int SetupType);
   void set (System.int SetupType, System.short value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SetupType`:

## VBA Syntax

See [ModelDoc2::PrintSetup](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~PrintSetup.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
