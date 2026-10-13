---
title: "PrintSetup Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "PrintSetup"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~PrintSetup.html"
---

# PrintSetup Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::PrintSetup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~PrintSetup.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property PrintSetup( _
   ByVal SetupType As System.Integer _
) As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
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

See [ModelDoc::PrintSetup](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~PrintSetup.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
