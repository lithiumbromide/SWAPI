---
title: "RunDesignCheck3 Method (ISWDesignCheck)"
project: "SOLIDWORKS Design Checker API Help"
interface: "ISWDesignCheck"
member: "RunDesignCheck3"
kind: "method"
source: "dsgnchkapi/SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck~RunDesignCheck3.html"
---

# RunDesignCheck3 Method (ISWDesignCheck)

Obsolete. Superseded by [ISWDesignCheck::RunDesignCheck4](SOLIDWORKS.Interop.dsgnchk~SOLIDWORKS.Interop.dsgnchk.ISWDesignCheck~RunDesignCheck4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub RunDesignCheck3( _
   ByVal StandardFileName As System.String, _
   ByRef status As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISWDesignCheck
Dim StandardFileName As System.String
Dim status As System.Integer

instance.RunDesignCheck3(StandardFileName, status)
```

### C#

```csharp
void RunDesignCheck3(
   System.string StandardFileName,
   ref System.int status
)
```

### C++/CLI

```cpp
void RunDesignCheck3(
   System.String^ StandardFileName,
   System.int% status
)
```

### Parameters

- `StandardFileName`:
- `status`:

## VBA Syntax

See [SWDesignCheck::RunDesignCheck3](ms-its:dsgnchkapivb6.chm::/DesignCheckerLib~SWDesignCheck~RunDesignCheck3.html).

## See Also

[ISWDesignCheck Interface](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck.html)
[ISWDesignCheck Members](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck_members.html)
