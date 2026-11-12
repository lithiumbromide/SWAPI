---
title: "IsSame Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IsSame"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsSame.html"
---

# IsSame Method (ISldWorks)

Gets whether the two specified objects are the same object.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsSame( _
   ByVal Object1 As System.Object, _
   ByVal Object2 As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Object1 As System.Object
Dim Object2 As System.Object
Dim value As System.Integer

value = instance.IsSame(Object1, Object2)
```

### C#

```csharp
System.int IsSame(
   System.object Object1,
   System.object Object2
)
```

### C++/CLI

```cpp
System.int IsSame(
   System.Object^ Object1,
   System.Object^ Object2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Object1`: Object
- `Object2`: Object

### Return Value

Object equality as defined by [swObjectEquality](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swObjectEquality.html)

## VBA Syntax

See [SldWorks::IsSame](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IsSame.html).

## Examples

[Compare Selected Objects and Their Persistent Reference IDs (VB.NET)](Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_VBNET.htm)
[Compare Selected Objects and Their Persistent Reference IDs (VBA)](Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_VB.htm)
[Compare Selected Objects and Their Persistent Reference IDs (C#)](Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_CSharp.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[IModelDocExtension::IsSamePersistentID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsSamePersistentID.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
