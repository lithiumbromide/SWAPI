---
title: "Next Method (IEnumComponents2)"
project: "SOLIDWORKS API Help"
interface: "IEnumComponents2"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2~Next.html"
---

# Next Method (IEnumComponents2)

Gets the next component in the components enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Component2, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumComponents2
Dim Celt As System.Integer
Dim Rgelt As Component2
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out Component2 Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] Component2^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`: Number of components for the components enumeration
- `Rgelt`: Pointer to an array [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) of size Celt
- `PceltFetched`: Pointer to the number of components returned from the list.; this value can be less than Celt if you ask for more components than exist, or it can be NULL if no more components exist

## VBA Syntax

See [EnumComponents2::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumComponents2~Next.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumComponents2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2.html)
[IEnumComponents2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
