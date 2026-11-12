---
title: "GetContactSetAt Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "GetContactSetAt"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~GetContactSetAt.html"
---

# GetContactSetAt Method (ICWContactManager)

Gets the contact set at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetContactSetAt( _
   ByVal NIndex As System.Integer _
) As CWContactSet
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim NIndex As System.Integer
Dim value As CWContactSet

value = instance.GetContactSetAt(NIndex)
```

### C#

```csharp
CWContactSet GetContactSetAt(
   System.int NIndex
)
```

### C++/CLI

```cpp
CWContactSet^ GetContactSetAt(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index of contact set

### Return Value

[Contact set](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet.html)

## VBA Syntax

See [CWContactManager::GetContactSetAt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~GetContactSetAt.html).

## Examples

[Copy Items to Another Study (VBA)](Copy_Items_to_Another_Study_Example_VB.htm)
[Copy Items to Another Study (VB.NET)](Copy_Items_to_Another_Study_Example_VBNET.htm)
[Copy Items to Another Study (C#)](Copy_Items_to_Another_Study_Example_CSharp.htm)

## Remarks

Before calling this method, call [ICWContactManager::ContactSetCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~ContactSetCount.html) to determine the value of NIndex.

If no contact set is present at the specified index, then this method returns Nothing or null with a non-0 error code.

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
