import React from "react";
import "./Navbar.css";
import {
  Navbar,
  NavbarBrand,
  NavbarContent,
  NavbarItem,
  Link,
  Button,
} from "@nextui-org/react";

import Logo from "../Logo/Logo";

const RocketNavbar = () => {
  return (
    <nav className="RocketNavbar">
      <Navbar className="flex justify-evenly w-full">
        <NavbarBrand>
          <Logo />
          <h1 className="font-bold text-inherit">RocketPal</h1>
        </NavbarBrand>
        <NavbarContent className="hidden sm:flex gap-8" justify="center">
          <NavbarItem isActive={false}>
            <Link color="foreground" href="/journals">
              Journals
            </Link>
          </NavbarItem>
          <NavbarItem isActive>
            <Link color="foreground" href="/therapist">
              Therapist
            </Link>
          </NavbarItem>
        </NavbarContent>
        <NavbarContent justify="end">
          <NavbarItem className="hidden lg:flex">
            <Link href="#">Login</Link>
          </NavbarItem>
          <NavbarItem>
            <div className="UserProfile"></div>
            <Button as={Link} color="primary" href="#" variant="flat">
              Sign Up
            </Button>
          </NavbarItem>
        </NavbarContent>
      </Navbar>
    </nav>
  );
};

export default RocketNavbar;
