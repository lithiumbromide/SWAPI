---
title: "VBA and SOLIDWORKS x64"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/VBA_and_SolidWorks_x64.htm"
---

# VBA and SOLIDWORKS x64

SOLIDWORKS 2013 SP0, and later, include a new version of Microsoft Visual Basic for Applications (VBA 7), which supports both 32-bit and 64-bit systems.

- **Declare** statements in VBA macros and applications created before the SOLIDWORKS 2013 release will not compile in VBA 7 on 64-bit systems. You must mark **Declare** statements as safe by using the **PtrSafe** attribute in your VBA macros and applications on 64-bit systems.

  Use the **LongPtr** variable type instead of the **Long** or **LongLong** variable types for function arguments representing pointers if your VBA macro or application must work with both 32-bit and 64-bit SOLIDWORKS.

  The **LongPtr** variable type and the **PtrSafe** attribute allow you to use the same **Declare** statement on either 32-bit or 64-bit systems.

- 32-bit ActiveX controls used by VBA macros with SOLIDWORKS 2012 and earlier:

  - must be recompiled on a 64-bit system.
  - will continue to work on a 32-bit system.

For more information about VBA 7, see Microsoft's:

- [Compatibility Between the 32-bit and 64-bit Versions of Office 2010](http://msdn.microsoft.com/en-us/library/ee691831.aspx)
- [Working with VBA in Office 2010 (32-bit) and Office 2010 (64-bit)](http://msdn.microsoft.com/en-us/library/ff700513(v=office.11).aspx)

See [Long vs. Integer](Long_vs_Integer.htm) for details about data types and SOLIDWORKS.
