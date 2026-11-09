
dark-calc:     file format elf64-x86-64


Disassembly of section .init:

0000000000401770 <_init>:
  401770:	48 83 ec 08          	sub    $0x8,%rsp
  401774:	48 8b 05 7d 18 20 00 	mov    0x20187d(%rip),%rax        # 602ff8 <__gmon_start__>
  40177b:	48 85 c0             	test   %rax,%rax
  40177e:	74 02                	je     401782 <_init+0x12>
  401780:	ff d0                	call   *%rax
  401782:	48 83 c4 08          	add    $0x8,%rsp
  401786:	c3                   	ret

Disassembly of section .plt:

0000000000401790 <.plt>:
  401790:	ff 35 72 18 20 00    	push   0x201872(%rip)        # 603008 <_GLOBAL_OFFSET_TABLE_+0x8>
  401796:	ff 25 74 18 20 00    	jmp    *0x201874(%rip)        # 603010 <_GLOBAL_OFFSET_TABLE_+0x10>
  40179c:	0f 1f 40 00          	nopl   0x0(%rax)

00000000004017a0 <strcpy@plt>:
  4017a0:	ff 25 72 18 20 00    	jmp    *0x201872(%rip)        # 603018 <strcpy@GLIBC_2.2.5>
  4017a6:	68 00 00 00 00       	push   $0x0
  4017ab:	e9 e0 ff ff ff       	jmp    401790 <.plt>

00000000004017b0 <puts@plt>:
  4017b0:	ff 25 6a 18 20 00    	jmp    *0x20186a(%rip)        # 603020 <puts@GLIBC_2.2.5>
  4017b6:	68 01 00 00 00       	push   $0x1
  4017bb:	e9 d0 ff ff ff       	jmp    401790 <.plt>

00000000004017c0 <strlen@plt>:
  4017c0:	ff 25 62 18 20 00    	jmp    *0x201862(%rip)        # 603028 <strlen@GLIBC_2.2.5>
  4017c6:	68 02 00 00 00       	push   $0x2
  4017cb:	e9 c0 ff ff ff       	jmp    401790 <.plt>

00000000004017d0 <mmap@plt>:
  4017d0:	ff 25 5a 18 20 00    	jmp    *0x20185a(%rip)        # 603030 <mmap@GLIBC_2.2.5>
  4017d6:	68 03 00 00 00       	push   $0x3
  4017db:	e9 b0 ff ff ff       	jmp    401790 <.plt>

00000000004017e0 <system@plt>:
  4017e0:	ff 25 52 18 20 00    	jmp    *0x201852(%rip)        # 603038 <system@GLIBC_2.2.5>
  4017e6:	68 04 00 00 00       	push   $0x4
  4017eb:	e9 a0 ff ff ff       	jmp    401790 <.plt>

00000000004017f0 <printf@plt>:
  4017f0:	ff 25 4a 18 20 00    	jmp    *0x20184a(%rip)        # 603040 <printf@GLIBC_2.2.5>
  4017f6:	68 05 00 00 00       	push   $0x5
  4017fb:	e9 90 ff ff ff       	jmp    401790 <.plt>

0000000000401800 <fprintf@plt>:
  401800:	ff 25 42 18 20 00    	jmp    *0x201842(%rip)        # 603048 <fprintf@GLIBC_2.2.5>
  401806:	68 06 00 00 00       	push   $0x6
  40180b:	e9 80 ff ff ff       	jmp    401790 <.plt>

0000000000401810 <memcpy@plt>:
  401810:	ff 25 3a 18 20 00    	jmp    *0x20183a(%rip)        # 603050 <memcpy@GLIBC_2.14>
  401816:	68 07 00 00 00       	push   $0x7
  40181b:	e9 70 ff ff ff       	jmp    401790 <.plt>

0000000000401820 <gets@plt>:
  401820:	ff 25 32 18 20 00    	jmp    *0x201832(%rip)        # 603058 <gets@GLIBC_2.2.5>
  401826:	68 08 00 00 00       	push   $0x8
  40182b:	e9 60 ff ff ff       	jmp    401790 <.plt>

0000000000401830 <fflush@plt>:
  401830:	ff 25 2a 18 20 00    	jmp    *0x20182a(%rip)        # 603060 <fflush@GLIBC_2.2.5>
  401836:	68 09 00 00 00       	push   $0x9
  40183b:	e9 50 ff ff ff       	jmp    401790 <.plt>

0000000000401840 <munmap@plt>:
  401840:	ff 25 22 18 20 00    	jmp    *0x201822(%rip)        # 603068 <munmap@GLIBC_2.2.5>
  401846:	68 0a 00 00 00       	push   $0xa
  40184b:	e9 40 ff ff ff       	jmp    401790 <.plt>

0000000000401850 <memmove@plt>:
  401850:	ff 25 1a 18 20 00    	jmp    *0x20181a(%rip)        # 603070 <memmove@GLIBC_2.2.5>
  401856:	68 0b 00 00 00       	push   $0xb
  40185b:	e9 30 ff ff ff       	jmp    401790 <.plt>

0000000000401860 <mprotect@plt>:
  401860:	ff 25 12 18 20 00    	jmp    *0x201812(%rip)        # 603078 <mprotect@GLIBC_2.2.5>
  401866:	68 0c 00 00 00       	push   $0xc
  40186b:	e9 20 ff ff ff       	jmp    401790 <.plt>

0000000000401870 <perror@plt>:
  401870:	ff 25 0a 18 20 00    	jmp    *0x20180a(%rip)        # 603080 <perror@GLIBC_2.2.5>
  401876:	68 0d 00 00 00       	push   $0xd
  40187b:	e9 10 ff ff ff       	jmp    401790 <.plt>

0000000000401880 <exit@plt>:
  401880:	ff 25 02 18 20 00    	jmp    *0x201802(%rip)        # 603088 <exit@GLIBC_2.2.5>
  401886:	68 0e 00 00 00       	push   $0xe
  40188b:	e9 00 ff ff ff       	jmp    401790 <.plt>

Disassembly of section .text:

0000000000401890 <_start>:
  401890:	31 ed                	xor    %ebp,%ebp
  401892:	49 89 d1             	mov    %rdx,%r9
  401895:	5e                   	pop    %rsi
  401896:	48 89 e2             	mov    %rsp,%rdx
  401899:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
  40189d:	50                   	push   %rax
  40189e:	54                   	push   %rsp
  40189f:	49 c7 c0 a0 1c 40 00 	mov    $0x401ca0,%r8
  4018a6:	48 c7 c1 30 1c 40 00 	mov    $0x401c30,%rcx
  4018ad:	48 c7 c7 0e 1c 40 00 	mov    $0x401c0e,%rdi
  4018b4:	ff 15 36 17 20 00    	call   *0x201736(%rip)        # 602ff0 <__libc_start_main@GLIBC_2.2.5>
  4018ba:	f4                   	hlt
  4018bb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000004018c0 <_dl_relocate_static_pie>:
  4018c0:	f3 c3                	repz ret
  4018c2:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
  4018c9:	00 00 00 
  4018cc:	0f 1f 40 00          	nopl   0x0(%rax)

00000000004018d0 <deregister_tm_clones>:
  4018d0:	55                   	push   %rbp
  4018d1:	b8 a0 30 60 00       	mov    $0x6030a0,%eax
  4018d6:	48 3d a0 30 60 00    	cmp    $0x6030a0,%rax
  4018dc:	48 89 e5             	mov    %rsp,%rbp
  4018df:	74 17                	je     4018f8 <deregister_tm_clones+0x28>
  4018e1:	b8 00 00 00 00       	mov    $0x0,%eax
  4018e6:	48 85 c0             	test   %rax,%rax
  4018e9:	74 0d                	je     4018f8 <deregister_tm_clones+0x28>
  4018eb:	5d                   	pop    %rbp
  4018ec:	bf a0 30 60 00       	mov    $0x6030a0,%edi
  4018f1:	ff e0                	jmp    *%rax
  4018f3:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
  4018f8:	5d                   	pop    %rbp
  4018f9:	c3                   	ret
  4018fa:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)

0000000000401900 <register_tm_clones>:
  401900:	be a0 30 60 00       	mov    $0x6030a0,%esi
  401905:	55                   	push   %rbp
  401906:	48 81 ee a0 30 60 00 	sub    $0x6030a0,%rsi
  40190d:	48 89 e5             	mov    %rsp,%rbp
  401910:	48 c1 fe 03          	sar    $0x3,%rsi
  401914:	48 89 f0             	mov    %rsi,%rax
  401917:	48 c1 e8 3f          	shr    $0x3f,%rax
  40191b:	48 01 c6             	add    %rax,%rsi
  40191e:	48 d1 fe             	sar    $1,%rsi
  401921:	74 15                	je     401938 <register_tm_clones+0x38>
  401923:	b8 00 00 00 00       	mov    $0x0,%eax
  401928:	48 85 c0             	test   %rax,%rax
  40192b:	74 0b                	je     401938 <register_tm_clones+0x38>
  40192d:	5d                   	pop    %rbp
  40192e:	bf a0 30 60 00       	mov    $0x6030a0,%edi
  401933:	ff e0                	jmp    *%rax
  401935:	0f 1f 00             	nopl   (%rax)
  401938:	5d                   	pop    %rbp
  401939:	c3                   	ret
  40193a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)

0000000000401940 <__do_global_dtors_aux>:
  401940:	80 3d 81 17 20 00 00 	cmpb   $0x0,0x201781(%rip)        # 6030c8 <completed.7698>
  401947:	75 17                	jne    401960 <__do_global_dtors_aux+0x20>
  401949:	55                   	push   %rbp
  40194a:	48 89 e5             	mov    %rsp,%rbp
  40194d:	e8 7e ff ff ff       	call   4018d0 <deregister_tm_clones>
  401952:	c6 05 6f 17 20 00 01 	movb   $0x1,0x20176f(%rip)        # 6030c8 <completed.7698>
  401959:	5d                   	pop    %rbp
  40195a:	c3                   	ret
  40195b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
  401960:	f3 c3                	repz ret
  401962:	0f 1f 40 00          	nopl   0x0(%rax)
  401966:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
  40196d:	00 00 00 

0000000000401970 <frame_dummy>:
  401970:	55                   	push   %rbp
  401971:	48 89 e5             	mov    %rsp,%rbp
  401974:	5d                   	pop    %rbp
  401975:	eb 89                	jmp    401900 <register_tm_clones>

0000000000401977 <input>:
  401977:	55                   	push   %rbp
  401978:	48 89 e5             	mov    %rsp,%rbp
  40197b:	48 83 ec 10          	sub    $0x10,%rsp
  40197f:	be 0f 00 00 00       	mov    $0xf,%esi
  401984:	bf e8 1c 40 00       	mov    $0x401ce8,%edi
  401989:	b8 00 00 00 00       	mov    $0x0,%eax
  40198e:	e8 5d fe ff ff       	call   4017f0 <printf@plt>
  401993:	48 8d 45 f0          	lea    -0x10(%rbp),%rax
  401997:	48 89 c7             	mov    %rax,%rdi
  40199a:	e8 81 fe ff ff       	call   401820 <gets@plt>
  40199f:	48 85 c0             	test   %rax,%rax
  4019a2:	74 0b                	je     4019af <input+0x38>
  4019a4:	48 8d 45 f0          	lea    -0x10(%rbp),%rax
  4019a8:	0f b6 00             	movzbl (%rax),%eax
  4019ab:	84 c0                	test   %al,%al
  4019ad:	75 14                	jne    4019c3 <input+0x4c>
  4019af:	bf d0 1c 40 00       	mov    $0x401cd0,%edi
  4019b4:	e8 f7 fd ff ff       	call   4017b0 <puts@plt>
  4019b9:	bf 00 00 00 00       	mov    $0x0,%edi
  4019be:	e8 bd fe ff ff       	call   401880 <exit@plt>
  4019c3:	48 8d 45 f0          	lea    -0x10(%rbp),%rax
  4019c7:	48 89 c6             	mov    %rax,%rsi
  4019ca:	bf d0 30 60 00       	mov    $0x6030d0,%edi
  4019cf:	e8 cc fd ff ff       	call   4017a0 <strcpy@plt>
  4019d4:	90                   	nop
  4019d5:	c9                   	leave
  4019d6:	c3                   	ret

00000000004019d7 <eval>:
  4019d7:	55                   	push   %rbp
  4019d8:	48 89 e5             	mov    %rsp,%rbp
  4019db:	48 83 ec 10          	sub    $0x10,%rsp
  4019df:	bf d0 30 60 00       	mov    $0x6030d0,%edi
  4019e4:	e8 d7 fd ff ff       	call   4017c0 <strlen@plt>
  4019e9:	48 83 f8 0f          	cmp    $0xf,%rax
  4019ed:	77 0c                	ja     4019fb <eval+0x24>
  4019ef:	bf d0 30 60 00       	mov    $0x6030d0,%edi
  4019f4:	e8 c7 fd ff ff       	call   4017c0 <strlen@plt>
  4019f9:	eb 05                	jmp    401a00 <eval+0x29>
  4019fb:	b8 0f 00 00 00       	mov    $0xf,%eax
  401a00:	89 45 fc             	mov    %eax,-0x4(%rbp)
  401a03:	8b 45 fc             	mov    -0x4(%rbp),%eax
  401a06:	83 c0 01             	add    $0x1,%eax
  401a09:	48 98                	cltq
  401a0b:	b9 d8 30 60 00       	mov    $0x6030d8,%ecx
  401a10:	48 89 c2             	mov    %rax,%rdx
  401a13:	be d0 30 60 00       	mov    $0x6030d0,%esi
  401a18:	48 89 cf             	mov    %rcx,%rdi
  401a1b:	e8 30 fe ff ff       	call   401850 <memmove@plt>
  401a20:	ba 08 00 00 00       	mov    $0x8,%edx
  401a25:	be c0 1c 40 00       	mov    $0x401cc0,%esi
  401a2a:	bf d0 30 60 00       	mov    $0x6030d0,%edi
  401a2f:	e8 dc fd ff ff       	call   401810 <memcpy@plt>
  401a34:	8b 45 fc             	mov    -0x4(%rbp),%eax
  401a37:	48 98                	cltq
  401a39:	48 83 c0 08          	add    $0x8,%rax
  401a3d:	48 05 d0 30 60 00    	add    $0x6030d0,%rax
  401a43:	0f b7 15 7f 02 00 00 	movzwl 0x27f(%rip),%edx        # 401cc9 <wrapper_back>
  401a4a:	66 89 10             	mov    %dx,(%rax)
  401a4d:	0f b6 15 77 02 00 00 	movzbl 0x277(%rip),%edx        # 401ccb <wrapper_back+0x2>
  401a54:	88 50 02             	mov    %dl,0x2(%rax)
  401a57:	be d0 30 60 00       	mov    $0x6030d0,%esi
  401a5c:	bf 10 1d 40 00       	mov    $0x401d10,%edi
  401a61:	b8 00 00 00 00       	mov    $0x0,%eax
  401a66:	e8 85 fd ff ff       	call   4017f0 <printf@plt>
  401a6b:	bf d0 30 60 00       	mov    $0x6030d0,%edi
  401a70:	e8 6b fd ff ff       	call   4017e0 <system@plt>
  401a75:	48 8b 05 24 16 20 00 	mov    0x201624(%rip),%rax        # 6030a0 <stdout@GLIBC_2.2.5>
  401a7c:	48 89 c7             	mov    %rax,%rdi
  401a7f:	e8 ac fd ff ff       	call   401830 <fflush@plt>
  401a84:	90                   	nop
  401a85:	c9                   	leave
  401a86:	c3                   	ret

0000000000401a87 <grade_eval>:
  401a87:	55                   	push   %rbp
  401a88:	48 89 e5             	mov    %rsp,%rbp
  401a8b:	48 83 ec 10          	sub    $0x10,%rsp
  401a8f:	89 7d fc             	mov    %edi,-0x4(%rbp)
  401a92:	83 7d fc 04          	cmpl   $0x4,-0x4(%rbp)
  401a96:	75 19                	jne    401ab1 <grade_eval+0x2a>
  401a98:	b8 45 00 00 00       	mov    $0x45,%eax
  401a9d:	2b 45 fc             	sub    -0x4(%rbp),%eax
  401aa0:	89 c6                	mov    %eax,%esi
  401aa2:	bf 20 1d 40 00       	mov    $0x401d20,%edi
  401aa7:	b8 00 00 00 00       	mov    $0x0,%eax
  401aac:	e8 3f fd ff ff       	call   4017f0 <printf@plt>
  401ab1:	48 8b 05 e8 15 20 00 	mov    0x2015e8(%rip),%rax        # 6030a0 <stdout@GLIBC_2.2.5>
  401ab8:	48 89 c7             	mov    %rax,%rdi
  401abb:	e8 70 fd ff ff       	call   401830 <fflush@plt>
  401ac0:	90                   	nop
  401ac1:	c9                   	leave
  401ac2:	c3                   	ret

0000000000401ac3 <main>:
  401ac3:	55                   	push   %rbp
  401ac4:	48 89 e5             	mov    %rsp,%rbp
  401ac7:	b8 00 00 00 00       	mov    $0x0,%eax
  401acc:	e8 a6 fe ff ff       	call   401977 <input>
  401ad1:	b8 00 00 00 00       	mov    $0x0,%eax
  401ad6:	e8 fc fe ff ff       	call   4019d7 <eval>
  401adb:	eb ea                	jmp    401ac7 <main+0x4>

0000000000401add <init_fixed_stack>:
  401add:	55                   	push   %rbp
  401ade:	48 89 e5             	mov    %rsp,%rbp
  401ae1:	48 83 ec 20          	sub    $0x20,%rsp
  401ae5:	48 c7 45 f8 00 20 80 	movq   $0x802000,-0x8(%rbp)
  401aec:	00 
  401aed:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
  401af1:	41 b9 00 00 00 00    	mov    $0x0,%r9d
  401af7:	41 b8 ff ff ff ff    	mov    $0xffffffff,%r8d
  401afd:	b9 22 00 10 00       	mov    $0x100022,%ecx
  401b02:	ba 07 00 00 00       	mov    $0x7,%edx
  401b07:	48 89 c6             	mov    %rax,%rsi
  401b0a:	48 bf 00 00 00 00 10 	movabs $0x721000000000,%rdi
  401b11:	72 00 00 
  401b14:	e8 b7 fc ff ff       	call   4017d0 <mmap@plt>
  401b19:	48 89 45 f0          	mov    %rax,-0x10(%rbp)
  401b1d:	48 83 7d f0 ff       	cmpq   $0xffffffffffffffff,-0x10(%rbp)
  401b22:	75 14                	jne    401b38 <init_fixed_stack+0x5b>
  401b24:	bf 48 1d 40 00       	mov    $0x401d48,%edi
  401b29:	e8 42 fd ff ff       	call   401870 <perror@plt>
  401b2e:	bf 01 00 00 00       	mov    $0x1,%edi
  401b33:	e8 48 fd ff ff       	call   401880 <exit@plt>
  401b38:	48 b8 00 00 00 00 10 	movabs $0x721000000000,%rax
  401b3f:	72 00 00 
  401b42:	48 39 45 f0          	cmp    %rax,-0x10(%rbp)
  401b46:	74 44                	je     401b8c <init_fixed_stack+0xaf>
  401b48:	48 8b 05 71 15 20 00 	mov    0x201571(%rip),%rax        # 6030c0 <stderr@GLIBC_2.2.5>
  401b4f:	48 8b 55 f0          	mov    -0x10(%rbp),%rdx
  401b53:	48 b9 00 00 00 00 10 	movabs $0x721000000000,%rcx
  401b5a:	72 00 00 
  401b5d:	be 70 1d 40 00       	mov    $0x401d70,%esi
  401b62:	48 89 c7             	mov    %rax,%rdi
  401b65:	b8 00 00 00 00       	mov    $0x0,%eax
  401b6a:	e8 91 fc ff ff       	call   401800 <fprintf@plt>
  401b6f:	48 8b 55 f8          	mov    -0x8(%rbp),%rdx
  401b73:	48 8b 45 f0          	mov    -0x10(%rbp),%rax
  401b77:	48 89 d6             	mov    %rdx,%rsi
  401b7a:	48 89 c7             	mov    %rax,%rdi
  401b7d:	e8 be fc ff ff       	call   401840 <munmap@plt>
  401b82:	bf 01 00 00 00       	mov    $0x1,%edi
  401b87:	e8 f4 fc ff ff       	call   401880 <exit@plt>
  401b8c:	48 8b 45 f0          	mov    -0x10(%rbp),%rax
  401b90:	48 89 45 e8          	mov    %rax,-0x18(%rbp)
  401b94:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
  401b98:	48 05 00 10 80 00    	add    $0x801000,%rax
  401b9e:	48 89 45 e0          	mov    %rax,-0x20(%rbp)
  401ba2:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
  401ba6:	ba 00 00 00 00       	mov    $0x0,%edx
  401bab:	be 00 10 00 00       	mov    $0x1000,%esi
  401bb0:	48 89 c7             	mov    %rax,%rdi
  401bb3:	e8 a8 fc ff ff       	call   401860 <mprotect@plt>
  401bb8:	83 f8 ff             	cmp    $0xffffffff,%eax
  401bbb:	75 14                	jne    401bd1 <init_fixed_stack+0xf4>
  401bbd:	bf a0 1d 40 00       	mov    $0x401da0,%edi
  401bc2:	e8 a9 fc ff ff       	call   401870 <perror@plt>
  401bc7:	bf 01 00 00 00       	mov    $0x1,%edi
  401bcc:	e8 af fc ff ff       	call   401880 <exit@plt>
  401bd1:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
  401bd5:	ba 00 00 00 00       	mov    $0x0,%edx
  401bda:	be 00 10 00 00       	mov    $0x1000,%esi
  401bdf:	48 89 c7             	mov    %rax,%rdi
  401be2:	e8 79 fc ff ff       	call   401860 <mprotect@plt>
  401be7:	83 f8 ff             	cmp    $0xffffffff,%eax
  401bea:	75 14                	jne    401c00 <init_fixed_stack+0x123>
  401bec:	bf c0 1d 40 00       	mov    $0x401dc0,%edi
  401bf1:	e8 7a fc ff ff       	call   401870 <perror@plt>
  401bf6:	bf 01 00 00 00       	mov    $0x1,%edi
  401bfb:	e8 80 fc ff ff       	call   401880 <exit@plt>
  401c00:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
  401c04:	48 89 05 e5 14 20 00 	mov    %rax,0x2014e5(%rip)        # 6030f0 <fixed_stack_top>
  401c0b:	90                   	nop
  401c0c:	c9                   	leave
  401c0d:	c3                   	ret

0000000000401c0e <__wrap_main>:
  401c0e:	41 54                	push   %r12
  401c10:	49 89 e4             	mov    %rsp,%r12
  401c13:	48 8b 25 d6 14 20 00 	mov    0x2014d6(%rip),%rsp        # 6030f0 <fixed_stack_top>
  401c1a:	e8 a4 fe ff ff       	call   401ac3 <main>
  401c1f:	4c 89 e4             	mov    %r12,%rsp
  401c22:	41 5c                	pop    %r12
  401c24:	c3                   	ret
  401c25:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
  401c2c:	00 00 00 
  401c2f:	90                   	nop

0000000000401c30 <__libc_csu_init>:
  401c30:	41 57                	push   %r15
  401c32:	41 56                	push   %r14
  401c34:	49 89 d7             	mov    %rdx,%r15
  401c37:	41 55                	push   %r13
  401c39:	41 54                	push   %r12
  401c3b:	4c 8d 25 c6 11 20 00 	lea    0x2011c6(%rip),%r12        # 602e08 <__frame_dummy_init_array_entry>
  401c42:	55                   	push   %rbp
  401c43:	48 8d 2d ce 11 20 00 	lea    0x2011ce(%rip),%rbp        # 602e18 <__do_global_dtors_aux_fini_array_entry>
  401c4a:	53                   	push   %rbx
  401c4b:	41 89 fd             	mov    %edi,%r13d
  401c4e:	49 89 f6             	mov    %rsi,%r14
  401c51:	4c 29 e5             	sub    %r12,%rbp
  401c54:	48 83 ec 08          	sub    $0x8,%rsp
  401c58:	48 c1 fd 03          	sar    $0x3,%rbp
  401c5c:	e8 0f fb ff ff       	call   401770 <_init>
  401c61:	48 85 ed             	test   %rbp,%rbp
  401c64:	74 20                	je     401c86 <__libc_csu_init+0x56>
  401c66:	31 db                	xor    %ebx,%ebx
  401c68:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
  401c6f:	00 
  401c70:	4c 89 fa             	mov    %r15,%rdx
  401c73:	4c 89 f6             	mov    %r14,%rsi
  401c76:	44 89 ef             	mov    %r13d,%edi
  401c79:	41 ff 14 dc          	call   *(%r12,%rbx,8)
  401c7d:	48 83 c3 01          	add    $0x1,%rbx
  401c81:	48 39 dd             	cmp    %rbx,%rbp
  401c84:	75 ea                	jne    401c70 <__libc_csu_init+0x40>
  401c86:	48 83 c4 08          	add    $0x8,%rsp
  401c8a:	5b                   	pop    %rbx
  401c8b:	5d                   	pop    %rbp
  401c8c:	41 5c                	pop    %r12
  401c8e:	41 5d                	pop    %r13
  401c90:	41 5e                	pop    %r14
  401c92:	41 5f                	pop    %r15
  401c94:	c3                   	ret
  401c95:	90                   	nop
  401c96:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
  401c9d:	00 00 00 

0000000000401ca0 <__libc_csu_fini>:
  401ca0:	f3 c3                	repz ret

Disassembly of section .fini:

0000000000401ca4 <_fini>:
  401ca4:	48 83 ec 08          	sub    $0x8,%rsp
  401ca8:	48 83 c4 08          	add    $0x8,%rsp
  401cac:	c3                   	ret
