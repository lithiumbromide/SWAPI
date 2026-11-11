---
title: "CompareObjects Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "CompareObjects"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~CompareObjects.html"
---

# CompareObjects Method (IEntityHelper)

Compares the two specified entities.

## Syntax

### Visual Basic

```vb
Function CompareObjects( _
   ByVal Obj1 As System.Object, _
   ByVal Obj2 As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool CompareObjects(
   System.object Obj1,
   System.object Obj2
)
```

### JScript

```
function CompareObjects(
   Obj1 : System.Object,
   Obj2 : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool CompareObjects(
   System.Object* Obj1,
   System.Object* Obj2
)
```

### C++/CLI

```cpp
System.bool CompareObjects(
   System.Object^ Obj1,
   System.Object^ Obj2
)
```

### Parameters

- `Obj1`: Entity to compare to Obj2
- `Obj2`: Entity to compare to Obj1

### Return Value

True if Obj1 and Obj2 are identical, false if not

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)

## Availability

DraftSight V1R4.0
