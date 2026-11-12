---
title: "GetContactComponentAt Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "GetContactComponentAt"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~GetContactComponentAt.html"
---

# GetContactComponentAt Method (ICWContactManager)

Gets the component contact at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetContactComponentAt( _
   ByVal NIndex As System.Integer _
) As CWContactComponent
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim NIndex As System.Integer
Dim value As CWContactComponent

value = instance.GetContactComponentAt(NIndex)
```

### C#

```csharp
CWContactComponent GetContactComponentAt(
   System.int NIndex
)
```

### C++/CLI

```cpp
CWContactComponent^ GetContactComponentAt(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index

### Return Value

[Component contact](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactComponent.html)

## VBA Syntax

See [CWContactManager::GetContactComponentAt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~GetContactComponentAt.html).

## Remarks

Before calling this method, call [ICWContactManager::ContactComponentCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~ContactComponentCount.html) to determine the value of NIndex.

If no contact is present at the specified index, then this method returns null with a non-zero error code.

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
