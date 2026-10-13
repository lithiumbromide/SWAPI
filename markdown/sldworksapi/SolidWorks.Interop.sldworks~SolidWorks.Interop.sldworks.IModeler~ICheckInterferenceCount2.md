---
title: "ICheckInterferenceCount2 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICheckInterferenceCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount2.html"
---

# ICheckInterferenceCount2 Method (IModeler)

Obsolete. Superseded by [IModeler::ICheckInterferenceCount3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICheckInterferenceCount3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICheckInterferenceCount2( _
   ByVal Body1 As Body2, _
   ByVal Body2 As Body2, _
   ByVal CoincidentInterference As System.Boolean, _
   ByRef Body1InterferedFaceCount As System.Integer, _
   ByRef Body2InterferedFaceCount As System.Integer, _
   ByRef IntersectedBodyCount As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Body1 As Body2
Dim Body2 As Body2
Dim CoincidentInterference As System.Boolean
Dim Body1InterferedFaceCount As System.Integer
Dim Body2InterferedFaceCount As System.Integer
Dim IntersectedBodyCount As System.Integer
Dim value As System.Boolean

value = instance.ICheckInterferenceCount2(Body1, Body2, CoincidentInterference, Body1InterferedFaceCount, Body2InterferedFaceCount, IntersectedBodyCount)
```

### C#

```csharp
System.bool ICheckInterferenceCount2(
   Body2 Body1,
   Body2 Body2,
   System.bool CoincidentInterference,
   out System.int Body1InterferedFaceCount,
   out System.int Body2InterferedFaceCount,
   out System.int IntersectedBodyCount
)
```

### C++/CLI

```cpp
System.bool ICheckInterferenceCount2(
   Body2^ Body1,
   Body2^ Body2,
   System.bool CoincidentInterference,
   [Out] System.int Body1InterferedFaceCount,
   [Out] System.int Body2InterferedFaceCount,
   [Out] System.int IntersectedBodyCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Body1`: First [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to check for interference
- `Body2`: Second [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to check for interference
- `CoincidentInterference`: True to check for coincident interference, false to not
- `Body1InterferedFaceCount`: Number of faces that are interfering that belong to the body passed in the first parameter of this method
- `Body2InterferedFaceCount`: Number of faces that are interfering that belong to the body passed in the second parameter of this method
- `IntersectedBodyCount`: Number of intersection bodies produced from this intersection

### Return Value

True if successful, false if not

## VBA Syntax

See [Modeler::ICheckInterferenceCount2](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICheckInterferenceCount2.html).

## Remarks

Call [IModeler::ICheckInterference2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICheckInterference2.html) after calling this method.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CheckInterference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference.html)
[IAssembyDoc::ToolsCheckInterference2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ToolsCheckInterference2.html)
[IAssembyDoc::IToolsCheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
