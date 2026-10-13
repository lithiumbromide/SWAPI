---
title: "Next Method (IEnumComponents)"
project: "SOLIDWORKS API Help"
interface: "IEnumComponents"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents~Next.html"
---

# Next Method (IEnumComponents)

Obsolete. Superseded by [IEnumComponents2::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumComponents2~Next.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Component, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumComponents
Dim Celt As System.Integer
Dim Rgelt As Component
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out Component Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] Component^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`:
- `Rgelt`:
- `PceltFetched`:

## VBA Syntax

See [EnumComponents::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumComponents~Next.html).

## See Also

[IEnumComponents Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents.html)
[IEnumComponents Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents_members.html)
