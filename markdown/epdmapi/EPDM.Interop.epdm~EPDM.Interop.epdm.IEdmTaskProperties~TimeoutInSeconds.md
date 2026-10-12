---
title: "TimeoutInSeconds Property (IEdmTaskProperties)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskProperties"
member: "TimeoutInSeconds"
kind: "property"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~TimeoutInSeconds.html"
---

# TimeoutInSeconds Property (IEdmTaskProperties)

Gets the number of seconds to wait until failing the task.

## Syntax

### Visual Basic

```vb
ReadOnly Property TimeoutInSeconds As System.Integer
```

### C#

```csharp
System.int TimeoutInSeconds {get;}
```

### C++/CLI

```cpp
property System.int TimeoutInSeconds {
   System.int get();
}
```

### Property Value

Number of seconds to wait until failing the task; 0 to wait forever

## See Also

[IEdmTaskProperties Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html)
[IEdmTaskProperties Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
