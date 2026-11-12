---
title: "ICheckInterferenceCount Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICheckInterferenceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount.html"
---

# ICheckInterferenceCount Method (IModeler)

Obsolete. Superseded by [IModeler::ICheckInterferenceCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICheckInterferenceCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICheckInterferenceCount( _
   ByVal Body1 As Body, _
   ByVal Body2 As Body, _
   ByVal CoincidentInterference As System.Boolean, _
   ByRef Body1InterferedFaceCount As System.Integer, _
   ByRef Body2InterferedFaceCount As System.Integer, _
   ByRef IntersectedBodyCount As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Body1 As Body
Dim Body2 As Body
Dim CoincidentInterference As System.Boolean
Dim Body1InterferedFaceCount As System.Integer
Dim Body2InterferedFaceCount As System.Integer
Dim IntersectedBodyCount As System.Integer
Dim value As System.Boolean

value = instance.ICheckInterferenceCount(Body1, Body2, CoincidentInterference, Body1InterferedFaceCount, Body2InterferedFaceCount, IntersectedBodyCount)
```

### C#

```csharp
System.bool ICheckInterferenceCount(
   Body Body1,
   Body Body2,
   System.bool CoincidentInterference,
   out System.int Body1InterferedFaceCount,
   out System.int Body2InterferedFaceCount,
   out System.int IntersectedBodyCount
)
```

### C++/CLI

```cpp
System.bool ICheckInterferenceCount(
   Body^ Body1,
   Body^ Body2,
   System.bool CoincidentInterference,
   [Out] System.int Body1InterferedFaceCount,
   [Out] System.int Body2InterferedFaceCount,
   [Out] System.int IntersectedBodyCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Body1`:
- `Body2`:
- `CoincidentInterference`:
- `Body1InterferedFaceCount`:
- `Body2InterferedFaceCount`:
- `IntersectedBodyCount`:

## VBA Syntax

See [Modeler::ICheckInterferenceCount](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICheckInterferenceCount.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
